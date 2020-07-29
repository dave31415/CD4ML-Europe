def get_feature_importance_emsemble(trained_model, encoder, print_features=True):
    importances = list(trained_model.feature_importances_)
    n = len(importances)
    names = [encoder.index_to_column(i) for i in range(n)]
    feature_importance = {k: v for k, v in zip(names, importances)}

    if print_features:
        importance_pairs = sorted(feature_importance.items(), key=lambda x: -x[1])
        print('Feature Importance')
        print("-" * 40)
        for pair in importance_pairs:
            print(pair)

    return feature_importance


def get_feature_importance_linear_model(trained_model, encoder, print_features=True):
    coef = trained_model.coef_
    intercept = trained_model.intercept_
    n = len(coef)
    names = [encoder.index_to_column(i) for i in range(n)]
    importances = coef.copy()
    feature_importance = {k: v for k, v in zip(names, importances)}

    if print_features:
        print('intercept', intercept)
        importance_pairs = sorted(feature_importance.items(), key=lambda x: -x[1])
        print('Feature Importance')
        print("-" * 40)
        for pair in importance_pairs:
            print(pair)

    return feature_importance


def get_feature_importance(trained_model, model_name, encoder, print_features=True):
    if model_name in ['random_forest', 'gradient_boosting', 'adaboost']:
        return get_feature_importance_emsemble(trained_model, encoder, print_features=print_features)
    elif model_name in ['ridge', 'lasso']:
        return get_feature_importance_linear_model(trained_model, encoder, print_features=print_features)
    else:
        return None