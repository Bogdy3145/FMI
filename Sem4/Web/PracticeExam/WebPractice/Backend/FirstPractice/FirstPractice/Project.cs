using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.DataAnnotations;

namespace FirstPractice
{
    public class Project
    {
        [Key]   
        public int Id { get; set; }
        public int ProjectManagerID { get; set; } // Foreign key for SoftwareDeveloper
        public string Name { get; set; } = string.Empty;
        public string Description { get; set; } = string.Empty;
        public string Members { get; set; }

        public SoftwareDeveloper ProjectManager { get; set; } = null!;
    }
}
