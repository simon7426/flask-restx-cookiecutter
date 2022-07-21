import os
import shutil
import json

MANIFEST = "manifest.json"


def delete_resources_for_disabled_features():
    with open(MANIFEST) as manifest_file:
        manifest = json.load(manifest_file)
        print(manifest)
        for feature in manifest['features']:
            if not feature['status']=="yes":
                print(f"removing resources for disabled feature {feature['name']}...")
                for resource in feature['resources']:
                    delete_resource(resource)
    print ("cleanup complete, removing manifest...")
    delete_resource(MANIFEST)


def delete_resource(resource):
    if os.path.isfile(resource):
        print("removing file: {}".format(resource))
        os.remove(resource)
    elif os.path.isdir(resource):
        print("removing directory: {}".format(resource))
        shutil.rmtree(resource)

if __name__ == "__main__":
    delete_resources_for_disabled_features()