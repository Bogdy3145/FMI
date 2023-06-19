using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.DataAnnotations;
namespace FirstPractice
{
    public class SoftwareDeveloper
    {
        [Key]
        public int Id { get; set; }
        public string Name { get; set; } = string.Empty;
        public int age { get; set; }
        public string Skills { get; set; } = string.Empty;

        public ICollection<Project> Projects { get; set; } = null!;
    }
}
