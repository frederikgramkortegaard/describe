# Service : YOLOv5
Pipes a given base64 string through a YOLOv5 object detection model and
    returns the results as a JSON object.
    
    Args:
        info: A request object (a JSON request-body) with a field "base64" containing a base64-encoded image as a string.
    Returns:
        JSON object containing the detection results
