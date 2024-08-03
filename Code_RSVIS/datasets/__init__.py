from datasets.RS18.refer_rsvis_dataset import ReferRSVIS


def build_dataset(image_set, dataset_name, **kwargs):
    if dataset_name == 'EndoVis-RS18':
        return ReferRSVIS(image_set, **kwargs)
    elif dataset_name == 'EndoVis-RS17':  
        return ReferRSVIS(image_set, **kwargs)
    raise ValueError(f'dataset {dataset_name} not supported')
