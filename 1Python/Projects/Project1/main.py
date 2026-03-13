from client import APIClient

client = APIClient()

# Create
new_post = client.create("posts", {"title": "Hello", "body": "World", "userId": 1})
print(new_post)

# Read
post = client.read("posts",1)
print(post)

# Update
updated_post = client.update("posts", 1, {"title": "Updated Title"})
print(updated_post)

# Delete
client.delete("posts", 1)
print("Post deleted")
