import os
import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split

def split_data(source_dir, train_dir, test_dir, test_size=0.2, random_state=42):
    """
    Split data from source directory into train and test sets.
    
    Args:
        source_dir: Path to the source data directory (e.g., 'data/Fruit Freshness Dataset')
        train_dir: Path where train data will be saved
        test_dir: Path where test data will be saved
        test_size: Proportion of data to use for testing (default: 0.2)
        random_state: Random seed for reproducibility
    """
    source_path = Path(source_dir)
    train_path = Path(train_dir)
    test_path = Path(test_dir)
    
    # Create train and test directories
    train_path.mkdir(parents=True, exist_ok=True)
    test_path.mkdir(parents=True, exist_ok=True)
    
    # Iterate through each fruit type
    for fruit_type in source_path.iterdir():
        if not fruit_type.is_dir():
            continue
            
        print(f"Processing {fruit_type.name}...")
        
        # Process each freshness category (Fresh/Rotten)
        for freshness in fruit_type.iterdir():
            if not freshness.is_dir():
                continue
                
            # Get all image files
            image_files = []
            for ext in ['*.jpg', '*.jpeg', '*.png', '*.webp', '*.jfif']:
                image_files.extend(list(freshness.glob(ext)))
            
            if len(image_files) == 0:
                print(f"  No images found in {freshness}")
                continue
            
            # Split into train and test
            train_files, test_files = train_test_split(
                image_files, 
                test_size=test_size, 
                random_state=random_state
            )
            
            # Create directories in train and test
            train_category_dir = train_path / fruit_type.name / freshness.name
            test_category_dir = test_path / fruit_type.name / freshness.name
            train_category_dir.mkdir(parents=True, exist_ok=True)
            test_category_dir.mkdir(parents=True, exist_ok=True)
            
            # Copy train files
            for file in train_files:
                shutil.copy2(file, train_category_dir / file.name)
            
            # Copy test files
            for file in test_files:
                shutil.copy2(file, test_category_dir / file.name)
            
            print(f"  {freshness.name}: {len(train_files)} train, {len(test_files)} test")

if __name__ == "__main__":
    # Define paths
    source_dir = "/Users/raghavmehta/Downloads/Fruit-Freshness-Classification/data/data"
    train_dir = "data/train"
    test_dir = "data/test"
    
    # Split the data (80% train, 20% test)
    split_data(source_dir, train_dir, test_dir, test_size=0.2, random_state=42)
    
    print("\nData split complete!")
    print(f"Train data: {train_dir}")
    print(f"Test data: {test_dir}")