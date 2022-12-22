import python_pachyderm

if __name__ == '__main__':
    # Connects to a pachyderm cluster on localhost:30650
    client = python_pachyderm.Client()

    # Create a pachyderm repo called `test`
    client.create_repo("test")

    # Create a file in (repo="test", branch="master") at `/dir_a/data.txt`
    # Similar to `pachctl put file test@master:/dir_a/data.txt`
    with client.commit("test", "master") as commit:
        client.put_file_bytes(commit, "/dir_a/data.txt", b"hello world")

    # Get the file
    f = client.get_file(("test", "master"), "/dir_a/data.txt")
    print(f.read())  # >>> b"hello world"
