function attachJsonHelpers() {
  var fields = document.querySelectorAll('[data-json-field]');
  fields.forEach(function (field) {
    var formatBtn = field.parentElement.querySelector('[data-json-format]');
    var sampleBtn = field.parentElement.querySelector('[data-json-sample]');
    if (formatBtn) {
      formatBtn.addEventListener('click', function () {
        try {
          var parsed = JSON.parse(field.value || '{}');
          field.value = JSON.stringify(parsed, null, 2);
        } catch (err) {
          alert('Invalid JSON: ' + err.message);
        }
      });
    }
    if (sampleBtn) {
      sampleBtn.addEventListener('click', function () {
        field.value = sampleBtn.dataset.sample;
      });
    }
  });

  var blocksFields = document.querySelectorAll('[data-blocks-field]');
  blocksFields.forEach(function (field) {
    if (!field.value) {
      field.value = '{"blocks": []}';
    }
  });

  var bodyFields = document.querySelectorAll('[data-body-field]');
  bodyFields.forEach(function (field) {
    if (!field.value) {
      field.value = '{"root":{"children":[]}}';
    }
  });
}

document.addEventListener('DOMContentLoaded', attachJsonHelpers);
