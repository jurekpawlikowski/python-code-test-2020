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
    return json_response(
        status=200,
        response_data={"data": {"comment": comment.serialize()}},
    )


@comment_blueprint.route("", methods=["POST"])
def create_comment():
    """
    Create a comment
    """
    data = json.loads(request.data)
    try:
        comment = Comment(
            season=data["season"],
            episode=data["episode"],
            content=data["content"],
            author_name=data["author_name"]
        )
    except KeyError as e:
        return json_response(status=400, response_data={"error": f"Your payload is missing {e.args[0]} field"})

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
    try:
        comment.content = data["content"]
        comment.author_name = data["author_name"]
    except KeyError as e:
        return json_response(status=400, response_data={"error": f"Your payload is missing {e.args[0]} field"})
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
