```c#
using System;
using System.IO.Pipes;
using System.Security.AccessControl;
using System.Security.Principal;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Xml.Serialization;

namespace FileOperations
{
    public class Person
    {
        public string Name { get; set; }
        public int Age { get; set; }
    }

    public class PersonWithProperty
    {
        [JsonPropertyName("f_name")]
        public string Name { get; set; }

        [JsonPropertyName("f_age")]
        public int Age { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // read
            string filePath = @"C:\Users\admin\Desktop\1.txt";
            if (File.Exists(filePath))
            {
                // read all content
                string content = File.ReadAllText(filePath);
                Console.WriteLine("File content is:");
                Console.WriteLine(content);

                // read all line
                string[] lines = File.ReadAllLines(filePath);
                foreach(string line in lines)
                {
                    Console.WriteLine(line);
                }

                // line by line
                // using会自动释放资源（基于 IDisposable）,这里是reader.Dispose()
                using (StreamReader reader = new StreamReader(filePath))
                {
                    string line;
                    while ((line = reader.ReadLine()) != null)
                    {
                        Console.WriteLine(line);
                    }
                }

            } 
            else
            {
                Console.WriteLine("File does not exist.");
            }

            // write
            string filePath1 = @"C:\Users\admin\Desktop\2.txt";
            string content1 = "helloworld\n123";
            File.WriteAllText(filePath1, content1);
            Console.WriteLine("Text written to file.");

            // write by line
            using(StreamWriter writer = new StreamWriter(filePath1))
            {
                writer.WriteLine("Hello");
                writer.WriteLine("Hello2");
                writer.WriteLine("Hello3");
            }


            // stream read by byte
            using (FileStream fs = new FileStream(filePath1, FileMode.Open))
            {
                byte[] buffer = new byte[1024];
                int bytesRead = fs.Read(buffer, 0, buffer.Length);
                Console.WriteLine($"Read {bytesRead} bytes.");
                // Convert bytes to string and display.
                string content = System.Text.Encoding.UTF8.GetString(buffer, 0, bytesRead);
                Console.WriteLine(content);
            }

            // stream write by byte
            using(FileStream fs = new FileStream(filePath, FileMode.Create))
            {
                string content = "stream write by byte";
                byte[] buffer = System.Text.Encoding.UTF8.GetBytes(content);
                fs.Write(buffer, 0, buffer.Length);
            }

            // seek
            using(FileStream fs = new FileStream(filePath, FileMode.Open))
            {
                // Read from the beginning.
                byte[] buffer1 = new byte[5];
                fs.Read(buffer1, 0, buffer1.Length);

                // Seek to the beginning.
                fs.Seek(0, SeekOrigin.Begin);

                // Read again.
                byte[] buffer2 = new byte[5];
                fs.Read(buffer2, 0, buffer2.Length);
            }

            AsyncFun();

            ErrorHandle();

            SerializeXml();

            SerialzeJson();

            //FileAndDirectory();

            PathBufferMemoryStreamExample();

            SecureFileOperations();
        }

        private static void SecureFileOperations()
        {
            string filePath = @"C:\Users\admin\Desktop\3.txt";
            using (StreamWriter sw = new StreamWriter(filePath))
            {
                sw.WriteLine("hello");
            }
            // Secure the File
            FileSecurity fileSecurity = new FileSecurity();
            SecurityIdentifier everyone = new SecurityIdentifier(WellKnownSidType.WorldSid, null);
            fileSecurity.AddAccessRule(new FileSystemAccessRule(everyone, FileSystemRights.Read, AccessControlType.Allow));
            
            FileInfo fileinfo = new FileInfo(filePath);
            FileSystemAclExtensions.SetAccessControl(fileinfo, fileSecurity);
            fileSecurity = FileSystemAclExtensions.GetAccessControl(fileinfo);
            
            foreach (FileSystemAccessRule rule in fileSecurity.GetAccessRules(true, true, typeof(SecurityIdentifier)))
            {
                Console.WriteLine($"Identity:{ rule.IdentityReference.Value}, Right: { rule.FileSystemRights},Type: {{rule.AccessControlType}}");
            }
        }

        private static void PathBufferMemoryStreamExample()
        {
            // Working with Paths
            string folder = @"C:\Users\admin\Desktop\";
            string fileName = "1.txt";
            string fullPath = Path.Combine(folder, fileName);
            Console.WriteLine($"Full Path: {fullPath}");

            // Create some data as a buffer
            byte[] buffer = new byte[1024]; // 1 KB buffer
            for (int i = 0; i < buffer.Length; i++)
            {
                buffer[i] = (byte)(i % 256);
            }

            // Working with Memory Stream
            using (MemoryStream memoryStream = new MemoryStream())
            {
                // Write the buffer to the memory stream
                memoryStream.Write(buffer, 0, buffer.Length);

                // Reset the position of the stream to the beginning
                memoryStream.Seek(0, SeekOrigin.Begin);

                // Read from the memory stream back into a new buffer
                byte[] readBuffer = new byte[1024];
                memoryStream.Read(readBuffer, 0, readBuffer.Length);
                for (int i = 0; i < buffer.Length; i++)
                {
                    if (buffer[i] != readBuffer[i])
                    {
                        Console.WriteLine("Buffers are not equal!");
                        return;
                    }
                }
                Console.WriteLine("Buffers are equal!");
            }
        }

        private static void FileAndDirectory()
        {
            File.Create("example.txt");
            bool exists = File.Exists("example.txt");
            string content = File.ReadAllText("example.txt");
            File.WriteAllText("example.txt", "Hello World!");
            File.Delete("example.txt");

            Directory.CreateDirectory("NewFolder");
            bool exists1 = Directory.Exists("NewFolder");
            string[] files = Directory.GetFiles("NewFolder");
            string[] dirs = Directory.GetDirectories("NewFolder");
            Directory.Delete("NewFolder", true);
        }

        private static void SerialzeJson()
        {
            Person person = new Person { Name = "Alice", Age = 30 };

            // Serialize to JSON
            string jsonString = JsonSerializer.Serialize(person);
            Console.WriteLine("Serialized JSON:");
            Console.WriteLine(jsonString);

            // Deserialize from JSON
            Person deserializedPerson = JsonSerializer.Deserialize<Person>(jsonString);
            Console.WriteLine($"Deserialized Person: Name = {deserializedPerson.Name}, Age = {deserializedPerson.Age}");
        }

        private static void SerializeXml()
        {
            Person person = new Person { Name = "Alice", Age = 30 };

            // Serialize object to XML
            XmlSerializer serializer = new XmlSerializer(typeof(Person));
            using (StringWriter writer = new StringWriter())
            {
                serializer.Serialize(writer, person);
                string xmlstring = writer.ToString();
                Console.WriteLine("Serialized XML:");
                Console.WriteLine(xmlstring);
            }

            // Deserialize object from XML
            string xmlInput = "<Person><Name>Alice</Name><Age>30</Age></Person > ";
            using (StringReader reader = new StringReader(xmlInput))
            {
                Person deserializedPerson = (Person)serializer.Deserialize(reader);
                Console.WriteLine($"p.name={deserializedPerson.Name},age={deserializedPerson.Age}");
            }
        }

        private static void ErrorHandle()
        {
            try
            {
                string text = File.ReadAllText("nonexistent.txt");
            }
            catch(FileNotFoundException e)
            {
                Console.WriteLine($"File not found: {e.Message}");
            }
            catch (UnauthorizedAccessException e)
            {
                Console.WriteLine($"Access denied: {e.Message}");
            }
            catch (IOException e)
            {
                Console.WriteLine($"I/O error: { e.Message}");
            }
            catch (Exception e)
            {
                Console.WriteLine($"Unexpected error: {e.Message}");
            }
            finally
            {

            }
        }

        private static async Task AsyncFun()
        {
            string filePath = @"C:\Users\admin\Desktop\1.txt";
            using (FileStream fs = new FileStream(filePath, FileMode.Open))
            {
                byte[] buffer = new byte[1024];
                int bytesRead = await fs.ReadAsync(buffer, 0, buffer.Length);
                Console.WriteLine($"Read {bytesRead} bytes.");
                string content = System.Text.Encoding.UTF8.GetString(buffer, 0, bytesRead);
                Console.WriteLine(content);
            }

        }
    }




}
```
