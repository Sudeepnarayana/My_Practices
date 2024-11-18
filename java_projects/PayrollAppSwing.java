import javax.swing.*;

import java.awt.event.*;

public class PayrollAppSwing {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Payroll System");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(350, 300);
        
        JPanel panel = new JPanel();
        frame.add(panel);
        placeComponents(panel);
        
        frame.setVisible(true);
    }
    
    private static void placeComponents(JPanel panel) {
        panel.setLayout(null);
        
        // Labels for employee details
        JLabel nameLabel = new JLabel("Employee Name:");
        nameLabel.setBounds(10, 20, 120, 25);
        panel.add(nameLabel);
        
        JTextField nameField = new JTextField(20);
        nameField.setBounds(140, 20, 165, 25);
        panel.add(nameField);
        
        JLabel empIdLabel = new JLabel("Employee ID:");
        empIdLabel.setBounds(10, 50, 120, 25);
        panel.add(empIdLabel);
        
        JTextField empIdField = new JTextField(20);
        empIdField.setBounds(140, 50, 165, 25);
        panel.add(empIdField);
        
        JLabel basicSalaryLabel = new JLabel("Basic Salary:");
        basicSalaryLabel.setBounds(10, 80, 120, 25);
        panel.add(basicSalaryLabel);
        
        JTextField basicSalaryField = new JTextField(20);
        basicSalaryField.setBounds(140, 80, 165, 25);
        panel.add(basicSalaryField);
        
        // Button to calculate salary
        JButton calculateButton = new JButton("Calculate Salary");
        calculateButton.setBounds(10, 110, 150, 25);
        panel.add(calculateButton);
        
        // Labels to display results
        JLabel hraLabel = new JLabel("HRA: ");
        hraLabel.setBounds(10, 140, 300, 25);
        panel.add(hraLabel);
        
        JLabel daLabel = new JLabel("DA: ");
        daLabel.setBounds(10, 170, 300, 25);
        panel.add(daLabel);
        
        JLabel taxLabel = new JLabel("Tax: ");
        taxLabel.setBounds(10, 200, 300, 25);
        panel.add(taxLabel);
        
        JLabel netSalaryLabel = new JLabel("Net Salary: ");
        netSalaryLabel.setBounds(10, 230, 300, 25);
        panel.add(netSalaryLabel);
        
        // Add action listener to the button
        calculateButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    // Retrieve inputs from text fields
                    String name = nameField.getText();
                    int empId = Integer.parseInt(empIdField.getText());
                    double basicSalary = Double.parseDouble(basicSalaryField.getText());
                    
                    // Create an Employee object
                    Employee emp = new Employee(name, empId, basicSalary);
                    
                    // Calculate individual values
                    double hra = emp.getHra();
                    double da = emp.getDa();
                    double tax = emp.calculateTax();
                    double netSalary = emp.calculateNetSalary();
                    
                    // Update the labels with the calculated values
                    hraLabel.setText("HRA: " + hra);
                    daLabel.setText("DA: " + da);
                    taxLabel.setText("Tax: " + tax);
                    netSalaryLabel.setText("Net Salary: " + netSalary);
                } catch (NumberFormatException ex) {
                    // Handle invalid input
                    hraLabel.setText("HRA: Invalid input");
                    daLabel.setText("DA: Invalid input");
                    taxLabel.setText("Tax: Invalid input");
                    netSalaryLabel.setText("Net Salary: Invalid input");
                }
            }
        });
    }
}
