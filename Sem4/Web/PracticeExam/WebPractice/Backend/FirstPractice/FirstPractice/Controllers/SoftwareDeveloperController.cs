using FirstPractice.Data;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
//using System.Data.Entity;
using Microsoft.EntityFrameworkCore;


namespace FirstPractice.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class SoftwareDeveloperController : ControllerBase
    {
        private readonly DataContext _context;
        public SoftwareDeveloperController(DataContext context)
        {
            _context = context;
        }

        [HttpGet]

        public async Task<ActionResult<List<SoftwareDeveloper>>> GetSoftwareDevelopers()
        {
            return Ok(await _context.SoftwareDevelopers.ToListAsync());
        }

        [HttpPost]

        public async Task<ActionResult<List<SoftwareDeveloper>>> CreateSoftwareDeveloper(SoftwareDeveloper dev)
        {
            _context.SoftwareDevelopers.Add(dev);
            await _context.SaveChangesAsync();

            return Ok(await _context.SoftwareDevelopers.ToListAsync());
        }

        [HttpPut]

        public async Task<ActionResult<List<SoftwareDeveloper>>> UpdateSoftwareDeveloper(SoftwareDeveloper dev)
        {
            var dbDev = await _context.SoftwareDevelopers.FindAsync(dev.Id);
            if (dbDev == null)
            {
                return BadRequest("Dev not found. ");

            }

            dbDev.Name = dev.Name;
            dbDev.age = dev.age;
            dbDev.Skills = dev.Skills;

            await _context.SaveChangesAsync();

            return Ok(await _context.SoftwareDevelopers.ToListAsync());
        }

        [HttpDelete("{id}")]

        public async Task<ActionResult<List<SoftwareDeveloper>>> DeleteSoftwareDeveloper(int id)
        {
            var dbDev = await _context.SoftwareDevelopers.FindAsync(id);

            if (dbDev != null)
            {
                return BadRequest("Dev not found. ");
            }

            _context.SoftwareDevelopers.Remove(dbDev);
            await _context.SaveChangesAsync();

            return Ok(await _context.SoftwareDevelopers.ToListAsync());


        }
    }

    ////////////////////////////Project Controller ////////////////////////
    ///

    [Route("api/[controller]")]
    [ApiController]
    public class ProjectController : ControllerBase {

        private readonly DataContext _context;

        public ProjectController(DataContext context)
        {
            _context = context;
        }

        [HttpGet]

        public async Task<ActionResult<List<Project>>> GetProjects()
        {
            return Ok(await _context.Projects.ToListAsync());
        }


        [HttpPost]

        public async Task<ActionResult<List<Project>>> CreateProject(Project pj)
        {
            _context.Projects.Add(pj);
            await _context.SaveChangesAsync();

            return Ok(await _context.Projects.ToListAsync());
        }

        [HttpPut]

        public async Task<ActionResult<List<Project>>> UpdateProject(Project pj)
        {
            var dbDev = await _context.Projects.FindAsync(pj.Id);
            if (dbDev == null)
            {
                return BadRequest("Pj not found. ");

            }

            dbDev.Name = pj.Name;
            dbDev.Description = pj.Description;
            dbDev.Members = pj.Members;
            dbDev.ProjectManagerID = pj.ProjectManagerID;

            await _context.SaveChangesAsync();

            return Ok(await _context.Projects.ToListAsync());
        }

        [HttpDelete("{id}")]

        public async Task<ActionResult<List<Project>>> DeleteProject(int id)
        {
            var dbDev = await _context.Projects.FindAsync(id);

            if (dbDev != null)
            {
                return BadRequest("Pj not found. ");
            }

            _context.Projects.Remove(dbDev);
            await _context.SaveChangesAsync();

            return Ok(await _context.Projects.ToListAsync());


        }
    }
    
}
