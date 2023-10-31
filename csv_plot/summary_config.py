from typing import List, Dict, Tuple

class MetricSummaryConfig:
    def __init__(self, metric: str = '',
                 filter_to_apply: Dict[str, list] = {},
                 groupby: List[List[str]] = [],
                 summary_columns: List[str] = ["value"]) -> None:
        """Constructor of a MetricSummaryConfig
        To instrument the metric Summarizer, one can create these configs with:
        Args:
            metric (str): a string to be checked for inclusion in the file name,
                i.e. if the file name contains the given string, the
                MetricSummaryConfig will be selected.
            filter_to_apply (Dict[str, list]): a dictionary that configures the filtering,
                i.e. for an entry (c, [v1, v2]), filter the values v1 and v2 for
                the column c.
            groupby (list[list]): a list of lists with columns to group by and
                run the summary, i.e. each sublist defines which columns the
                summary will group and run the analysis on.
            summary_columns (List[str]): a list of columns to be summarized.
                Default is "Value".
        """
        self.metric = metric
        self.filter_to_apply = filter_to_apply
        self.groupby = groupby
        self.summary_columns = summary_columns