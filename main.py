from agent import Agent


def main():
    agent = Agent(
        skill_file_path="./skill.md" 
    )
    result = agent.run("What is the weather in New York")
    print(result)
    result = agent.run("What about Seattle?")
    print(result)



if __name__ == "__main__":
    main()
