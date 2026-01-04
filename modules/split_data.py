import os
import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split

def split_data(source_dir, train_dir, test_dir, test_size=0.2, random_state=42):
    source_path = Path(source_dir)
    train_path = Path(train_dir)
    test_path = Path(test_dir)
    
    train_path.mkdir(parents=True, exist_ok=True)
    test_path.mkdir(parents=True, exist_ok=True)
    
    for fruit_type in source_path.iterdir():
        if not fruit_type.is_dir():
            continue
            
        print(fruit_type.name)
        
        for freshness in fruit_type.iterdir():
            if not freshness.is_dir():
                continue
                
            image_files = []
            for ext in ['*.jpg', '*.jpeg', '*.png', '*.webp', '*.jfif']:
                image_files.extend(list(freshness.glob(ext)))
            
            if len(image_files) == 0:
                print(freshness)
                continue
            train_files, test_files = train_test_split(
                image_files, 
                test_size=test_size, 
                random_state=random_state
            )
            
            train_category_dir = train_path / fruit_type.name / freshness.name
            test_category_dir = test_path / fruit_type.name / freshness.name
            train_category_dir.mkdir(parents=True, exist_ok=True)
            test_category_dir.mkdir(parents=True, exist_ok=True)
            
            for file in train_files:
                shutil.copy2(file, train_category_dir / file.name)
            
            for file in test_files:
                shutil.copy2(file, test_category_dir / file.name)
            print(f"  {freshness.name}: {len(train_files)} train, {len(test_files)} test")

if __name__ == "__main__":
    
    source_dir = "/Users/raghavmehta/Downloads/Fruit-Freshness-Classification/data/data"
    train_dir = "data/train"
    test_dir = "data/test"
    
    split_data(source_dir, train_dir, test_dir, test_size=0.2, random_state=42)
    
    print("\nData split complete!")
    print(f"Train data: {train_dir}")
    print(f"Test data: {test_dir}")