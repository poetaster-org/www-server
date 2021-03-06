import graphene
from graphene import relay
from texts import models

from ..common.fields import (
    FilterableConnectionField,
)

from .types import (
    TextConnection,
    TextAnnotationConnection,
    SearchIndexedTextConnection,
    CollectionConnection
)

from .mutations import (
    TextUpdate,
    TextCreate,
    TextAnnotationRelationCreate
)


class TextsQueries(graphene.ObjectType):
    texts = FilterableConnectionField(
        TextConnection,
        slug=graphene.String())

    texts_search = relay.ConnectionField(
        SearchIndexedTextConnection,
        query=graphene.String())

    collections = FilterableConnectionField(
        CollectionConnection,
        slug=graphene.String())

    text_annotations = relay.ConnectionField(
        TextAnnotationConnection)

    def resolve_text_annotations(root, info):
        return models.session.query(models.TextLabel).all()

    def resolve_texts_search(root, info, query):
        return models.Text.search(query)


class TextsMutations(graphene.ObjectType):
    # text_update = TextUpdate.Field()
    text_create = TextCreate.Field()

    text_annotation_relation_create = TextAnnotationRelationCreate.Field()
