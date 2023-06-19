using Microsoft.EntityFrameworkCore;
using System;

namespace FirstPractice.Data;

public class DataContext : DbContext
{
    public DataContext(DbContextOptions<DataContext> options) : base(options) { }

    public DbSet<SoftwareDeveloper> SoftwareDevelopers => Set<SoftwareDeveloper>();
    public DbSet<Project> Projects => Set<Project>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Project>()
            .HasOne<SoftwareDeveloper>(p => p.ProjectManager)
            .WithMany(s => s.Projects)
            .HasForeignKey(b => b.ProjectManagerID);

        modelBuilder.Entity<SoftwareDeveloper>()
            .HasKey(p => p.Id);
    }
}


