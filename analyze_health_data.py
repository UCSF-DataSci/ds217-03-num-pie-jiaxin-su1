#!/usr/bin/env python3
"""
Health Sensor Data Analysis Script

Complete the TODO sections to analyze health sensor data using NumPy.
This script demonstrates basic NumPy operations for data loading, statistics,
filtering, and report generation.
"""

import numpy as np


def load_data(filename):
    """Load CSV data using NumPy.
    
    Args:
        filename: Path to CSV file
        
    Returns:
        NumPy structured array with all columns
    """
    # This code is provided because np.genfromtxt() is not covered in the lecture
    dtype = [('patient_id', 'U10'), ('timestamp', 'U20'), 
             ('heart_rate', 'i4'), ('blood_pressure_systolic', 'i4'),
             ('blood_pressure_diastolic', 'i4'), ('temperature', 'f4'),
             ('glucose_level', 'i4'), ('sensor_id', 'U10')]
    
    data = np.genfromtxt(filename, delimiter=',', dtype=dtype, skip_header=1)
    return data


def calculate_statistics(data):
    """
    Calculate basic statistics for numeric columns.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with statistics
    """
    # TODO: Calculate average heart rate using data['heart_rate'].mean()
    # TODO: Calculate average systolic BP using data['blood_pressure_systolic'].mean()
    # TODO: Calculate average glucose level using data['glucose_level'].mean()
    # TODO: Return as dictionary with keys: 'avg_heart_rate', 'avg_systolic_bp', 'avg_glucose'
   
    avg_heart_rate = data['heart_rate'].mean()
    avg_systolic_bp = data['blood_pressure_systolic'].mean()
    avg_glucose = data['glucose_level'].mean()

    return {
        'avg_heart_rate': f"{avg_heart_rate:.1f}",
        'avg_systolic_bp': f"{avg_systolic_bp:.1f}",
        'avg_glucose': f"{avg_glucose:.1f}"
    }
    return data
    
   


def find_abnormal_readings(data):
    """Find readings with abnormal values.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with counts
    """
    # TODO: Count readings where heart rate > 90 using boolean indexing
    # Example: high_hr_count = len(data[data['heart_rate'] > 90])
    # Or: high_hr_count = (data['heart_rate'] > 90).sum()
    high_hr_count = int((data['heart_rate'] > 90).sum())

    # TODO: Count readings where systolic BP > 130 using boolean indexing
    # Example: high_bp_count = len(data[data['blood_pressure_systolic'] > 130])
    high_bp_count = len(data[data['blood_pressure_systolic'] > 130])

    # TODO: Count readings where glucose > 110 using boolean indexing
    # Example: high_glucose_count = len(data[data['glucose_level'] > 110])
    high_glucose_count = len(data[data['glucose_level'] > 110])

    # TODO: Return dictionary with keys: 'high_heart_rate', 'high_blood_pressure', 'high_glucose'
    return {
        'high_heart_rate': high_hr_count,
        'high_blood_pressure': high_bp_count,
        'high_glucose': high_glucose_count
    }


def generate_report(stats, abnormal, total_readings):
    """Generate formatted analysis report.
    
    Args:
        stats: Dictionary of statistics
        abnormal: Dictionary of abnormal counts
        total_readings: Total number of readings
        
    Returns:
        Formatted string report
    """
    # TODO: Create a formatted report string using f-strings
    # TODO: Include all statistics with proper formatting using .1f for decimals
    # Example: f"Heart Rate: {stats['avg_heart_rate']:.1f} bpm"
    # TODO: Include section headers and labels for readability
    # TODO: Include total_readings, all averages, and all abnormal counts
    report = f"""Health Sensor Data Analysis Report
{'=' * 40}

Dataset Summary:
- Total readings: {total_readings}

Average Measurements:
- Heart Rate: {stats['avg_heart_rate']} bpm
- Systolic BP: {stats['avg_systolic_bp']} mmHg
- Glucose Level: {stats['avg_glucose']} mg/dL

Abnormal Readings:
- High Heart Rate (>90): {abnormal['high_heart_rate']} readings
- High Blood Pressure (>130): {abnormal['high_blood_pressure']} readings
- High Glucose (>110): {abnormal['high_glucose']} readings
"""
    return report

import os

def save_report(report, filename):
    """Save report to file.
    
    Args:
        report: Report string
        filename: Output filename
    """
    # TODO: Write the report to a file using open() with 'w' mode
    # Example: with open(filename, 'w') as f:
    #              f.write(report)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        f.write(report)


def main():
    """Main execution function."""
    # TODO: Load the data from 'health_data.csv' using load_data()
    # TODO: Calculate statistics using calculate_statistics()
    # TODO: Find abnormal readings using find_abnormal_readings()
    # TODO: Calculate total readings using len(data)
    # TODO: Generate report using generate_report()
    # TODO: Save to 'output/analysis_report.txt' using save_report()
    # TODO: Print success message
    data = load_data('health_data.csv')
    stats = calculate_statistics(data)
    abnormal = find_abnormal_readings(data)
    total_readings = len(data)
    report = generate_report(stats, abnormal, total_readings)
    save_report(report, 'output/analysis_report.txt')
    print("Analysis report saved to 'output/analysis_report.txt'.")

if __name__ == "__main__":
    main()