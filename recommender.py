import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM


def sample_recommendation(model, data, user_ids):
    n_users, n_items = data['train'].shape
    for user_id in user_ids:
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]
        scores = model.predict(user_id, np.arange(n_items))
        top_items = data['item_labels'][np.argsort(-scores)]
        print("User %s" % user_id)
        print(' Known positives:')

        for x in known_positives[:5]:
            print("\t %s" % x)

        print(' Recommended:')

        for x in top_items[:5]:
            print("\t %s" % x)


data = fetch_movielens(min_rating=4.0)
model = LightFM(loss='warp')
model.fit(data['train'], epochs=30, num_threads=2)

sample_recommendation(model, data, [3, 20, 451])
