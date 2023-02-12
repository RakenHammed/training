from abc import ABC, abstractmethod


class EntityRepository(ABC):
    @abstractmethod
    def get_by(self, _id):
        pass

    @abstractmethod
    def get_all_by(self, filters):
        pass

    @abstractmethod
    def create(self, entity):
        pass

    @abstractmethod
    def update(self, _id, entity):
        pass

    @abstractmethod
    def delete(self, _id):
        pass

    @staticmethod
    def _to_entity_from(row, entity):
        if row:
            for column in row.__table__.columns:
                setattr(entity, column.name, getattr(row, column.name))
            return entity
        return {}

    def _to_entities_from(self, rows, entity):
        entities = []
        if rows:
            for row in rows:
                entities.append(self._to_entity_from(row, entity))
        return entities
