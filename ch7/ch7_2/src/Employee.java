/* Employee is a super class for the Director, Manager, and Respondent classes. It is
 * is implemented as an abstract class since there should be no need to instantiate an Employee
 * type directly */
abstract class Employee {
    private Call currentCall = null;
    protected Rank rank;

    public Employee(CallHandler handler) { /* ... */ }

    /* Start the conversation */
    public void receiveCall(Call call) { /* ... */ }

    /* The issue is resolved, finish the call */
    public void callCompleted() { /* ... */ }

    /* The issue has not been resolved. Escalate the call, and assign to a new employee */
    public void escalateAndReassign() { /* ... */ }

    /* Assign a new call to an employee, if empoyee is free */
    public boolean assignNewCall() { /* ... */ }

    /* Return whether or not employee is free */
    public boolean isFree() { return currentCall == null; }

    public Rank getRank() { return rank; }
}
