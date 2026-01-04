import os
import shutil
from pathlib import Path

def reorganize_data(source_train, source_test, dest_train, dest_test):
    """
    Reorganizes data from nested structure to flat 6-class structure.
    
    Before: train/Apple/Fresh/, train/Apple/Rotten/
    After:  train/Apple_Fresh/, train/Apple_Rotten/
    
    Creates 6 classes:
    - Apple_Fresh
    - Apple_Rotten
    - Banana_Fresh
    - Banana_Rotten
    - Strawberry_Fresh
    - Strawberry_Rotten
    """
    
    def reorganize_split(source_dir, dest_dir):
        """Reorganize a single split (train or test)"""
        source = Path(source_dir)
        dest = Path(dest_dir)
        
        if not source.exists():
            print(f"Warning: Source directory {source} does not exist!")
            return
        
        # Create destination directory
        dest.mkdir(parents=True, exist_ok=True)
        
        # Process each fruit type (Apple, Banana, Strawberry)
        for fruit_folder in sorted(source.iterdir()):
            if not fruit_folder.is_dir():
                continue
            
            fruit_name = fruit_folder.name  # e.g., "Apple"
            
            # Process Fresh folder
            fresh_source = fruit_folder / "Fresh"
            if fresh_source.exists():
                class_name = f"{fruit_name}_Fresh"  # e.g., "Apple_Fresh"
                dest_class_dir = dest / class_name
                dest_class_dir.mkdir(parents=True, exist_ok=True)
                
                # Count and copy all image files
                image_count = 0
                for ext in ['*.jpg', '*.jpeg', '*.png', '*.webp', '*.jfif']:
                    for img in fresh_source.glob(ext):
                        if img.is_file():
                            shutil.copy2(img, dest_class_dir / img.name)
                            image_count += 1
                
                print(f"  ✓ {class_name}: {image_count} images")
            
            # Process Rotten folder
            rotten_source = fruit_folder / "Rotten"
            if rotten_source.exists():
                class_name = f"{fruit_name}_Rotten"  # e.g., "Apple_Rotten"
                dest_class_dir = dest / class_name
                dest_class_dir.mkdir(parents=True, exist_ok=True)
                
                # Count and copy all image files
                image_count = 0
                for ext in ['*.jpg', '*.jpeg', '*.png', '*.webp', '*.jfif']:
                    for img in rotten_source.glob(ext):
                        if img.is_file():
                            shutil.copy2(img, dest_class_dir / img.name)
                            image_count += 1
                
                print(f"  ✓ {class_name}: {image_count} images")
    
    # Reorganize train data
    print("Reorganizing TRAIN data...")
    reorganize_split(source_train, dest_train)
    
    # Reorganize test data
    print("\nReorganizing TEST data...")
    reorganize_split(source_test, dest_test)
    
    print("\n" + "="*50)
    print("Data reorganization complete!")
    print("="*50)
    print(f"Reorganized train data: {dest_train}")
    print(f"Reorganized test data: {dest_test}")
    print("\nYour data now has 6 classes:")
    print("  - Apple_Fresh")
    print("  - Apple_Rotten")
    print("  - Banana_Fresh")
    print("  - Banana_Rotten")
    print("  - Strawberry_Fresh")
    print("  - Strawberry_Rotten")


if __name__ == "__main__":
    # Define paths (adjust these to match your setup)
    source_train = "modules/data/train"
    source_test = "modules/data/test"
    
    # Destination directories (new organized structure)
    dest_train = "modules/data/train_organized"
    dest_test = "modules/data/test_organized"
    
    # Run the reorganization
    reorganize_data(
        source_train=source_train,
        source_test=source_test,
        dest_train=dest_train,
        dest_test=dest_test
    )