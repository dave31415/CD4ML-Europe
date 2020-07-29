from cd4ml.problems.groceries.features import feature_functions as ff

from cd4ml.feature_set import FeatureSet

feature_set_1_params = {'feature_set_name': 'feature_set_1',
                        'target_field': 'unit_sales',
                        'extra_information_fields': [],
                        'base_categorical_n_levels_dict': {'item_nbr': 8000,
                                                           'date': 10000},
                        'base_fields_numerical': [],
                        # omitted fields will not result in encoded variables
                        'derived_categorical_n_levels_dict': {'year': 100,
                                                              'month': 20,
                                                              'day_of_week': 20,
                                                              'product_class': 100,
                                                              'product_family': 100},
                        'derived_fields_numerical': ['day', 'day_off', 'days_until_end', 'transactions_in_day'],
                        'encoder_excluded_fields': [],
                        'encoder_untransformed_fields': ['date']}


class FeatureSet1(FeatureSet):
    def __init__(self, date_lookup, item_nbr_lookup):
        super(FeatureSet1, self).__init__()
        self.date_lookup = date_lookup
        self.item_nbr_lookup = item_nbr_lookup
        self.params = feature_set_1_params.copy()
    # actually derive the fields

    def derived_features_categorical(self, base_features):
        # some of these might not selected above
        date = base_features['date']
        year, month, day = ff.date_to_ymd(date)
        day_of_week = ff.date_to_day_of_week(base_features, self.date_lookup)

        product_class = ff.item_nbr_to_product_class(base_features, self.item_nbr_lookup)
        product_family = ff.item_nbr_to_product_family(base_features, self.item_nbr_lookup)

        features = {'year': year,
                    'month': month,
                    'day_of_week': day_of_week,
                    'product_class': product_class,
                    'product_family': product_family}

        return {k: features[k] for k in self.params['derived_categorical_n_levels_dict'].keys()}

    def derived_features_numerical(self, base_features):
        # some of these might not selected above

        date = base_features['date']
        year, month, day = ff.date_to_ymd(date)
        day_off = ff.date_to_day_off(base_features, self.date_lookup)
        days_until_end = ff.date_to_days_until_end(base_features, self.date_lookup)
        trans = ff.date_to_transactions(base_features, self.date_lookup)

        features = {'day': day,
                    'day_off': day_off,
                    'days_until_end': days_until_end,
                    'transactions_in_day': trans}

        return {k: features[k] for k in self.params['derived_fields_numerical']}