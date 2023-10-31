from hamcrest import *
import pytest

from csv_plot.summary_config import MetricSummaryConfig

@pytest.fixture
def empty_config():
    empty_config = MetricSummaryConfig()
    return empty_config

@pytest.fixture
def filled_config():
    metric = 'sample_metric'
    groupby = ['column1', ['column2', 'column3']]
    filter_to_apply = {'column1': ['value1'], 'column2': ['value2', 'value3']}
    summary_columns = ['column2', 'column3']
    config = MetricSummaryConfig(metric=metric,
                                       groupby=groupby,
                                       filter_to_apply=filter_to_apply,
                                       summary_columns=summary_columns)
    return config

def test_empty_config(empty_config):
    assert_that(empty_config.metric, equal_to(''))
    assert_that(empty_config.groupby, has_length(0))
    assert_that(empty_config.filter_to_apply, has_length(0))
    assert_that(empty_config.summary_columns, has_length(1) and equal_to(['value']))

def test_filled_config(filled_config):
    assert_that(filled_config.metric, equal_to('sample_metric'))
    assert_that(filled_config.groupby, has_length(2))
    assert_that(filled_config.filter_to_apply, has_length(2))
    assert_that(filled_config.summary_columns, has_length(2) and equal_to(['column2', 'column3']))