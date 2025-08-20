import yaml

def main():
    # Introductory question for blueprint name
    print("Welcome to the Blueprint Generator!")
    blueprint_name = input("What do you want to name your blueprint? ").strip()
    filename = f{blueprint_name}.yaml
    if not blueprint_name:
        print("Error: Please provide a valid blueprint name.")
        return
    
    description = input(f"Please enter a long form description for {blueprint_name}: ")
    
    # Version is hardcoded as per the original request
    version = "0.0.1"
    
    # Check if optional settings are desired
    want_optional_settings = input("Would you like to go over optional settings (modules, groups)? ").strip().lower()
    
    modules = []
    groups = []
    
    if want_optional_settings in ['yes', 'y']:
        print("\nOptional Settings:")
        
        while True:
            module_input = input("Enter any additional modules (comma-separated) or press Enter to skip: ")
            if not module_input.strip():
                break
            modules.extend([m.strip() for m in module_input.split(',')])
    
    # Kernel customization is hardcoded as per the original request
    kernel_append = "nosmt=force"
    
    # Create the blueprint dictionary
    blueprint = {
        'name': blueprint_name,
        'description': description,
        'version': version,
        'modules': modules,
        'groups': groups,
        'customizations': {
            'kernel': {'append': kernel_append}
        }
    }
    
    # Write to blueprint.yaml
    with open(filename, 'w') as file:
        yaml.dump(blueprint, file)
    
    print(f"\nBlueprint '{blueprint_name}' has been created successfully!")

if __name__ == "__main__":
    main()
