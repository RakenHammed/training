from app.entities.user_filters import UserFilters


class UserSqlAlchemyFiltersBuilder:
    def __init__(self, sql_alchemy_user_repository=None):
        self.__sql_alchemy_user_repository = sql_alchemy_user_repository

    def ids_filter(self, ids):
        return self.__sql_alchemy_user_repository.id.in_(ids)

    def emails_filter(self, emails):
        return self.__sql_alchemy_user_repository.email.in_(emails)

    def birth_date_is_superior_to(self, date_timestamp):
        return self.__sql_alchemy_user_repository.birthdate >= date_timestamp

    def build_from(self, filters: UserFilters):
        sql_alchemy_filters = []
        if filters.ids:
            sql_alchemy_filters.append(self.ids_filter(filters.ids))
        if filters.birth_date:
            sql_alchemy_filters.append(
                self.birth_date_is_superior_to(filters.birth_date)
            )
        if filters.emails:
            sql_alchemy_filters.append(self.emails_filter(filters.emails))
        return sql_alchemy_filters
