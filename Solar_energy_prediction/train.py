#train.py



model = RandomForestRegressor(n_estimators= 1400, max_features=5, criterion= 'absolute_error')

model.fit(X_train_all, y_train_all)

import pickle

with open("rand_forest_model.model", "wb") as archivo_salida:
    pickle.dump(model, archivo_salida)