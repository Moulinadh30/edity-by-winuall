const formValidator = (() => {
    const rules = {};
  
    // Function to add a new validation rule
    const addRule = (name, rule) => {
      rules[name] = rule;
    };
  
    // Function to validate a single input element
    const validateInput = (input) => {
      const validations = input.dataset.validate.split('|');
      let isValid = true;
      validations.forEach((validation) => {
        const [ruleName, ruleValue] = validation.split(':');
        const rule = rules[ruleName];
        const errorElement = input.nextElementSibling;
        if (rule && !rule(input.value, ruleValue)) {
          isValid = false;
          errorElement.textContent = input.dataset.error || 'Invalid input';
          errorElement.style.display = 'block';
        }
      });
      if (isValid) {
        const errorElement = input.nextElementSibling;
        errorElement.style.display = 'none';
      }
      return isValid;
    };
  
    // Function to validate the entire form
    const validateForm = (form) => {
      let isValid = true;
      const inputs = form.querySelectorAll('[data-validate]');
      inputs.forEach((input) => {
        if (!validateInput(input)) {
          isValid = false;
        }
      });
      return isValid;
    };
  
    return {
      addRule,
      validateForm,
    };
  })();
  
  // Adding validation rules
  formValidator.addRule('required', (value) => value.trim() !== '');
  formValidator.addRule('email', (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value));
  formValidator.addRule('minLength', (value, length) => value.length >= length);
  formValidator.addRule('maxLength', (value, length) => value.length <= length);
  formValidator.addRule('match', (value, matchValue) => value === document.getElementById(matchValue).value);
  
