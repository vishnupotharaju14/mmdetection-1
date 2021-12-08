from .coco import CocoDataset
from .registry import DATASETS
from .xml_style import XMLDataset
from .voc import VOCDataset
@DATASETS.register_module
class MyDataset(XMLDataset):

    # CLASSES =('Dent', 'Scratch_or_spot')#, 'Shatter', 'Tear')
    CLASSES = ('pothole')
