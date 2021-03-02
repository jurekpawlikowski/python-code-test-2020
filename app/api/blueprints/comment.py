import json

from flask import Blueprint, request

from app.api.models import Comment
from app.api.utlis.http import json_response

comment_blueprint = Blueprint("comment", __name__)


@comment_blueprint.route("<int:comment_id>", methods=["GET"])
def read_comment(comment_id: int):
    """
    Read details of a comment
    """
    comment = Comment.query.get(comment_id)
    if comment is None:
        return json_response(404)
    import pdb

    pdb.set_trace()
    return json_response(
        status=200,
        response_data={"data": {"comment": comment.serialize()}},
    )


@comment_blueprint.route("", methods=["POST"])
def create_comment():
    """
    Create a comment
    """
    comment = Comment(**json.loads(request.data))
    comment.save()
    return json_response(
        status=201,
        response_data={"data": {"comment": comment.serialize()}},
    )


@comment_blueprint.route("<int:comment_id>", methods=["PUT"])
def update_comment(comment_id: int):
    """
    Update a comment
    """
    data = json.loads(request.data)
    comment = Comment.query.get(comment_id)
    if comment is None:
        return json_response(404)
    comment.content = data["content"]
    comment.author_name = data["author_name"]
    comment.save()
    return json_response(
        status=200,
        response_data={"data": {"comment": comment.serialize()}},
    )


@comment_blueprint.route("<int:comment_id>", methods=["DELETE"])
def delete_comment(comment_id: int):
    """
    Delete a comment
    """
    comment = Comment.query.get(comment_id)
    if comment is None:
        return json_response(404)
    comment.delete()
    return json_response(status=200)
