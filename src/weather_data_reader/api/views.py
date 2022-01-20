import json
from urllib.error import HTTPError

import numpy as np
import pandas as pd
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Used function based views instead of class based views
# as response can be delivered without any model or serializer.
# Also, the problem statement only requires GET API.
@api_view(['GET'])
def get_weather_data(request):
    """
    An API to return summarised weather data from UK MetOffice.
    Takes region and weather as params, and outputs JSON.

    param request: request object having request params
    request param region : takes region as input
    request param parameter : takes weather parameter as input
    return: HTTP Response
    rtype: JSON
    """
    region = request.query_params.get('region', None)
    parameter = request.query_params.get('parameter', None)
    if region is None or parameter is None:     # Checks if both parameters are present
        return Response(
            'Please include both region and parameter in params',
            status=status.HTTP_400_BAD_REQUEST
        )
    else:
        url = (
            f'https://www.metoffice.gov.uk/pub/data/weather/'
            f'uk/climate/datasets/{parameter}/ranked/{region}.txt'
        )
        try:    # Checking if URL is valid
            df = pd.read_csv(
                url,
                sep=r'\s+',
                skiprows=5,
                storage_options={'User-Agent': 'Mozilla/5.0'}
            )
        except HTTPError:   # Throws HTTP 400 if URL is invalid
            return Response(
                'Please pass valid values for region and parameter',
                status=status.HTTP_400_BAD_REQUEST
            )
    df.columns = df.columns.str.split('.').str[0]

    out = df.groupby(np.repeat(np.arange(len(df.columns) // 2), 2), axis=1).apply(
            lambda x: x.set_index('year')
        ).droplevel(0, axis=1).reset_index()    # Removes duplicate year columns
    out = out.set_index(['year'])
    return Response(
        json.loads(out.to_json()),  # Returns JSON response
        status=status.HTTP_200_OK
    )
