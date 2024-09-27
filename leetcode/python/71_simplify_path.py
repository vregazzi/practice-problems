class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        while "." in parts:
            parts.remove(".")
        while "" in parts:
            parts.remove("")
        while ".." in parts:
            index = parts.index("..")
            if index != 0:
                parts = parts[:index - 1] + parts[index + 1:]
            else:
                parts.remove("..")
        return "/" + "/".join(parts)


if __name__ == "__main__":
    s = Solution()
    assert s.simplifyPath("/home//./user") == "/home/user"
    assert s.simplifyPath(
        "/home/user/Documents/../Pictures") == "/home/user/Pictures"
    assert s.simplifyPath("/a/../../b/../c//.//") == "/c"
