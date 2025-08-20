```c#

using System.Globalization;

Person person = new Person();
person.Name = "joha";
person.Age = 12;

person.Introduce();



public class Person
{
    // Properties
    public string Name { get; set; }
    public int Age { get; set; }

    private decimal price;
    public string Price
    {
        get { return $"${price: 0.00}"; }
        set { price = decimal.Parse(value, NumberStyles.Currency); }
    }

    public int m
    {
        get => m;
        set { m = value + 10; }
    }


    static public int A { get; set; }

    // Method
    public void Introduce()
    {
        Console.WriteLine($"Hello, i am {Name} and i am {Age} years old.");
    }

    // 构造函数，相当于 constructor
    //public Person(string name, int age)
    //{
    //    Name = name;
    //    Age = age;
    //}

    static void B()
    {
        Console.WriteLine($"{A}.");
    }

    public void DisplayGreeting(string name, string greeting = "Hello") { }

}


public class Professor : Person {
}

// 抽象类
public abstract class Animal
{
    public abstract void Speak();
    public abstract void Speak(string text);

}

public class Dog : Animal
{
    public override void Speak(){ }
    public override void Speak(string text){ }
}



public interface IProduct
{
    string Name { get; set; }
    decimal Price { get; set; }
}
public interface IRentable
{
    int RentalPeriodInDays { get; set; }
    void Rent();
}

public class Book : IProduct, IRentable
{
    public string Name { get; set; }
    public decimal Price { get; set; }
    public int RentalPeriodInDays { get; set; }
    public void Rent() { }
}
```
