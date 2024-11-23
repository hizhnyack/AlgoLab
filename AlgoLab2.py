
class RankingSystem:
    def __init__(self, num_features, feature_weights, objects_features):
        # Инициализация системы ранжирования с количеством признаков, весами признаков и признаками объектов
        self.num_features = num_features
        self.feature_weights = feature_weights
        self.objects_features = objects_features
        # Вычисление начальных значений релевантности для всех объектов
        self.relevance_scores = [self.calculate_relevance(object_idx) for object_idx in range(len(objects_features))]

    def calculate_relevance(self, object_idx):
        # Вычисление значения релевантности объекта на основе взвешенной суммы его признаков
        return sum(self.feature_weights[feature_idx] * self.objects_features[object_idx][feature_idx] for
                   feature_idx in range(self.num_features))

    def update_feature(self, object_idx, feature_idx, new_value):
        # Обновление конкретного признака объекта и пересчет его релевантности
        self.objects_features[object_idx][feature_idx] = new_value
        self.relevance_scores[object_idx] = self.calculate_relevance(object_idx)

    def get_top_k(self, k):
        # Получение индексов топ k объектов с наибольшими значениями релевантности
        sorted_indices = sorted(range(len(self.relevance_scores)), key=lambda idx: self.relevance_scores[idx], reverse=True)
        return [idx + 1 for idx in sorted_indices[:k]]

def main():
    # Входные данные
    num_features = 2
    feature_weights = [1, 100]
    num_objects = 10
    objects_features = [
        [1, 2],
        [2, 1],
        [3, 1],
        [4, 1],
        [5, 1],
        [6, 1],
        [7, 1],
        [8, 1],
        [9, 1],
        [10, 1]
    ]
    num_queries = 4
    queries = [
        "1 2",
        "1 10",
        "2 4 1 1000",
        "1 10"
    ]

    # Инициализация системы ранжирования
    ranking_system = RankingSystem(num_features, feature_weights, objects_features)

    # Обработка запросов
    results = []
    for query in queries:
        query_parts = list(map(int, query.split()))
        if query_parts[0] == 1:
            # Запрос типа 1: получить топ k релевантных объектов
            top_k = query_parts[1]
            results.append(" ".join(map(str, ranking_system.get_top_k(top_k))))
        elif query_parts[0] == 2:
            # Запрос типа 2: обновить значение признака
            object_idx, feature_idx, new_value = query_parts[1] - 1, query_parts[2] - 1, query_parts[3]
            ranking_system.update_feature(object_idx, feature_idx, new_value)

    # Печать результатов
    for result in results:
        print(result)


if __name__ == "__main__":
    main()