// Show ps like unix
int
ps()
{
  struct proc *p;

  sti();

  acquire(&ptable.lock);
  cprintf("name \t pid \t state \t \t nice \n");
  for (p = ptable.proc; p < &ptable.proc[NPROC]; p++){
      if ( p->state == SLEEPING )
          cprintf("%s \t %d  \t SLEEPING \t %d\n ", p->name, p->pid, p->nice);
      else if ( p->state == RUNNING )
          cprintf("%s \t %d  \t RUNNING \t %d\n ", p->name, p->pid, p->nice);
      else if ( p->state == RUNNABLE )
          cprintf("%s \t %d  \t RUNNABLE \t %d\n ", p->name, p->pid, p->nice);
  }
  release(&ptable.lock);

  return 25;
}