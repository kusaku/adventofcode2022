if __name__ == '__main__':
    with open('data.txt') as fh:
        total_calories = sorted(
            sum(
                map(
                    int,
                    filter(
                        None,
                        calories.split('\n')
                    )
                )
            ) for calories in fh.read().split('\n\n')
        )

        print(total_calories[-1])
        print(sum(total_calories[-3:]))
