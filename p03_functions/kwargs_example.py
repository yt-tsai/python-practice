# **kwargs example
# **kwargs collects multiple keyword arguments into a dictionary.


def show_profile(**profile):
    print(profile)
    for key, value in profile.items():
        print(f"{key}: {value}")


show_profile(
    name="Peter",
    language="Python",
    experience=10
)

