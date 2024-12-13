from task_1 import Book, BankAccount, SocialNetworkPost # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

if __name__ == "__main__":
    # TODO: инстанцировать все описанные классы, создав три объекта.
    book = Book("Python для продвинутых", "Сергей Сергеев", 350)
    account = BankAccount("Анна Иванова", 1000.0)
    post = SocialNetworkPost("Дмитрий Сидоров", "Замечательный день!")

    print(book.get_info())
    print(account.deposit(200.0))
    print(post.display_post())

    try:
        # Вызываем метод read_chapter с некорректным номером главы
        book.read_chapter(100)  # Больше чем предполагается глав по умолчанию
    except ValueError as e:
        print(f"Ошибка при чтении главы: {e}")

    try:
        # Вызываем метод deposit с отрицательной суммой
        account.deposit(-50.0)
    except ValueError as e:
        print(f"Ошибка при внесении средств: {e}")


    try:
        # Вызываем метод withdraw с суммой, превышающей баланс
        account.withdraw(2000.0)
    except ValueError as e:
        print(f"Ошибка при снятии средств: {e}")
