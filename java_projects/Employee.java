public class Employee {
    private String name;
    private int empId;
    private double basicSalary;
    private double hra; // House Rent Allowance
    private double da;  // Dearness Allowance
    private double tax;

    // Constructor
    public Employee(String name, int empId, double basicSalary) {
        this.name = name;
        this.empId = empId;
        this.basicSalary = basicSalary;
        this.hra = basicSalary * 0.10; // 10% of basic salary as HRA
        this.da = basicSalary * 0.15;  // 15% of basic salary as DA
    }

    // Calculate Gross Salary
    public double calculateGrossSalary() {
        return basicSalary + hra + da;
    }

    // Calculate Tax (simplified, fixed at 5% of gross salary)
    public double calculateTax() {
        return calculateGrossSalary() * 0.05; // 5% Tax on gross salary
    }

    // Calculate Net Salary
    public double calculateNetSalary() {
        tax = calculateTax();
        return calculateGrossSalary() - tax;
    }

    // Getter methods for HRA, DA, and Tax
    public double getHra() {
        return hra;
    }

    public double getDa() {
        return da;
    }

    public double getTax() {
        return tax;
    }

    // Getter methods for name and employee ID
    public String getName() {
        return name;
    }

    public int getEmpId() {
        return empId;
    }

    public double getBasicSalary() {
        return basicSalary;
    }
}
