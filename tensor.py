import tensorflow as tf

# Define the number of users and items
num_users = 100
num_items = 50

# Define the input layer for user and item IDs
user_input = tf.keras.layers.Input(shape=(1,))
item_input = tf.keras.layers.Input(shape=(1,))

# Define the embedding layer for user and item IDs
user_embedding = tf.keras.layers.Embedding(num_users, 10)(user_input)
item_embedding = tf.keras.layers.Embedding(num_items, 10)(item_input)

# Flatten the embedding layers
user_flatten = tf.keras.layers.Flatten()(user_embedding)
item_flatten = tf.keras.layers.Flatten()(item_embedding)

# Concatenate the flattened embeddings
concatenated = tf.keras.layers.Concatenate()([user_flatten, item_flatten])

# Define the output layer for the neural network
output = tf.keras.layers.Dense(1, activation='sigmoid')(concatenated)

# Create the model and compile it
model = tf.keras.models.Model(inputs=[user_input, item_input], outputs=output)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
