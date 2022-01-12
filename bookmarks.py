import mobie
import mobie.metadata as mm
import os
import json

root = './data'
datasets = mm.get_datasets(root)

def get_bookmarks_from_file(filepath,dataset,key='bookmarks'):

    with open(filepath) as f:
        b_content = json.load(f)

    if key in b_content.keys():
        bookmarks = b_content[key]
        for b_label,bookmark in bookmarks.items():
            for idx,sDisp in enumerate(bookmark['sourceDisplays']):
                bookmark['sourceDisplays'][idx]['imageDisplay']['color']="white"

            mm.add_view_to_dataset(dataset,b_label,bookmark)



for dataset in datasets:
    dataset = os.path.join(root,dataset)
    bookmark_dir = os.path.join(dataset, 'misc', 'bookmarks')
    for b_file in os.listdir(bookmark_dir):
        if b_file.endswith('.json'):
            get_bookmarks_from_file(os.path.join(bookmark_dir,b_file),dataset)
