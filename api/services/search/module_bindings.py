""" """

from typing import List, Dict


def get_function(name):
    """Attempts to find a function with the given name
    in the globals() namespace

    Args:
        name (str): The name of the function to look for

    Returns:
        The function if found, None otherwise
    """

    try:
        return globals()[name]
    except KeyError:
        print("KeyError : No such function {}".format(name))


def test_function_getter():
    """Tests the get_function function"""
    
    func = get_function("test_function_getter")
    if func is not None:
        print("test_function is {}".format(func))
    else:
        print("test_function is None")


def yolov5(metadata):
    """Performs YOLO V5 detection on the given metadata["image"]

    Args:
        metadata (dict): A dictionary of metadata

    Requires:
        metadata["image"] (str): A base64 encoded image

    Returns:
        An enriched dictionary of metadata
    """

    # @TODO : Implement the yolov5
    # @TODO : Add the yolov5 to the metadata
    # @TODO : Return the enriched metadata

    pass


def similarity(metadata: Dict):
    """Computes the similarity between a given image and an enriched search query in the metadata

    Args:
        metadata (dict): A dict of rich metadata

    Requires:
        metadata["image"] (dict): A dictionary of image metadata
        metadata["query"] (dict): A dictionary of search query metadata

    Returns:
        A float representing the similarity between the image and the search query
        bound between 0.0 and 1.0
    """

    # @TODO : Implement the similarity
    # @TODO : Add the similarity to the metadata
    # @TODO : Return the sorted list of metadata
    return metadata


def query(metadata: Dict):
    """Given a metadata dictionary, returns the enriched
    dictionary with the query and more extensive metadata
    as its tokens, context, stems, synonyms and word2vec
    encodings

    Args:
        metadata (dict): A sparse metadata dictionary

    Requires:
        metadata["query"] (str): A string representing the search query

    Returns:
        An enriched dictionary of metadata
    """

    # @TODO : Implement the query
    # @TODO : Add the query to the metadata
    # @TODO : Return the enriched metadata
    return metadata


def pipeline(metadata: List[Dict]):
    """Performs the image processing pipeline,
    calling on the available services in the pipeline,
    finally sorting and ranking all the given images.

    Args:
        metadata (list): A list of sparse metadata dictionaries

    Requires:
        metadata[n]["image"] (str): A base64 encoded image
        metadata[n]["query"] (str): A string representing the search query

    Returns:
        A sorted list of metadata dictionaries
    """

    # @TODO : Implement the pipeline
    # @TODO : Add the pipeline to the metadata
    # @TODO : Return the sorted list of metadata
    return metadata


if __name__ == "__main__":

    # Unit Tests
    test_function_getter()
