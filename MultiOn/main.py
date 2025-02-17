from multion.client import MultiOn
multion = MultiOn(api_key="MULTION_API_KEY")
browse = multion.browse(
    cmd="Find the top comment of the top post on Hackernews.",
    url="https://news.ycombinator.com/"
)
print("Browse response:", browse)
