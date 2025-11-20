import src.swiss_weatherdata.gbm as gbm
import pandas as pd


def test_get_smn_stations_info():

    df = gbm.get_stations_info(full_description=False, network='smn')
    nrows = df.shape[0]
    assert nrows > 1, "Empty DataFrame retrieved"


def test_get_nbcn_stations_info():

    df = gbm.get_stations_info(full_description=False, network='nbcn')
    nrows = df.shape[0]
    assert nrows > 1, "Empty DataFrame retrieved"


def test_get_smn_measures():

    df_expected = pd.read_pickle('tests/test_data_tre200h0_rre150h0_PAY.pickle')
    df = gbm.get_smn_measures(sta='PAY', parameters=['tre200h0', 'rre150h0'], beg='201001150600', end='201003011800')
    assert df_expected.equals(df), "Problem with SMN data retrieval"


def test_get_nbcn_measures():

    df_expected = pd.read_pickle('tests/test_data_th9120mv_GVE.pickle')
    df = gbm.get_nbcn_measures(sta='GVE', parameters=['th9120mv'], beg='198301010000', end='202512310000')
    assert df_expected.equals(df), "Problem with NBCN data retrieval"


