(function () {
  'use strict';

  // ─── Helpers ────────────────────────────────────────────────
  function safeJsonParse(str) {
    if (!str || str === 'null' || str === 'undefined') return null;
    try { return JSON.parse(str); } catch (e) { return null; }
  }

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    if (attrs) {
      Object.keys(attrs).forEach(function (k) {
        if (k === 'className') node.className = attrs[k];
        else if (k === 'textContent') node.textContent = attrs[k];
        else if (k === 'innerHTML') node.innerHTML = attrs[k];
        else node.setAttribute(k, attrs[k]);
      });
    }
    if (children) {
      (Array.isArray(children) ? children : [children]).forEach(function (c) {
        if (c) node.appendChild(typeof c === 'string' ? document.createTextNode(c) : c);
      });
    }
    return node;
  }

  var ICONS = {
    drag: '<svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor"><circle cx="5" cy="4" r="1.5"/><circle cx="11" cy="4" r="1.5"/><circle cx="5" cy="8" r="1.5"/><circle cx="11" cy="8" r="1.5"/><circle cx="5" cy="12" r="1.5"/><circle cx="11" cy="12" r="1.5"/></svg>',
    collapse: '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 5l4 4 4-4"/></svg>',
    expand: '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 9l-4-4-4 4"/></svg>',
    remove: '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 3L3 11M3 3l8 8"/></svg>',
    plus: '<svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 1v10M1 6h10"/></svg>',
  };

  var BLOCK_LABELS = {
    rich_text:       'Rich Text',
    code:            'Code / Embed',
    cta:             'CTA',
    callout:         'Callout',
    feature_grid:    'Feature Grid',
    faq:             'FAQ',
    quote:           'Quote',
    comparison_table:'Comparison Table',
    pricing_table:   'Pricing Table',
    logo_cloud:      'Logo Cloud',
    image_gallery:   'Image Gallery',
    table:           'Table',
  };

  var BLOCK_TYPES = Object.keys(BLOCK_LABELS);

  // ─── Block Defaults ──────────────────────────────────────────
  function blockDefaults(type) {
    switch (type) {
      case 'rich_text':       return { type: type, content: { blocks: [] } };
      case 'code':            return { type: type, html: '' };
      case 'cta':             return { type: type, title: '', body: '', button_label: '', button_url: '' };
      case 'callout':         return { type: type, title: '', body: '' };
      case 'feature_grid':    return { type: type, items: [{ title: '', body: '' }] };
      case 'faq':             return { type: type, items: [{ question: '', answer: '' }] };
      case 'quote':           return { type: type, quote: '', author: '' };
      case 'comparison_table':return { type: type, headers: ['Feature', 'Plan A', 'Plan B'], rows: [['', '', '']] };
      case 'pricing_table':   return { type: type, plans: [{ title: '', price: '', features: [''] }] };
      case 'logo_cloud':      return { type: type, logos: [{ src: '', alt: '' }] };
      case 'image_gallery':   return { type: type, title: '', layout: 'grid', images: [{ src: '', alt: '', caption: '' }] };
      case 'table':           return { type: type, headers: [], rows: [['']] };
      default:                return { type: type };
    }
  }

  // ─── Field Builders ──────────────────────────────────────────
  function fieldInput(label, value, onChange, placeholder) {
    var input = el('input', { type: 'text', value: value || '', placeholder: placeholder || '' });
    input.addEventListener('input', function () { onChange(input.value); });
    var lbl = el('label', { textContent: label });
    var wrap = el('div', { className: 'cms-field' }, [lbl, input]);
    return wrap;
  }

  function fieldTextarea(label, value, onChange, placeholder) {
    var ta = el('textarea', { placeholder: placeholder || '' });
    ta.value = value || '';
    ta.addEventListener('input', function () { onChange(ta.value); });
    var lbl = el('label', { textContent: label });
    var wrap = el('div', { className: 'cms-field' }, [lbl, ta]);
    return wrap;
  }

  // ─── Block Type Renderers ────────────────────────────────────
  function renderCtaFields(block, sync) {
    var wrap = el('div');
    wrap.appendChild(fieldInput('Title', block.title, function (v) { block.title = v; sync(); }));
    wrap.appendChild(fieldTextarea('Body', block.body, function (v) { block.body = v; sync(); }));
    wrap.appendChild(fieldInput('Button Label', block.button_label, function (v) { block.button_label = v; sync(); }));
    wrap.appendChild(fieldInput('Button URL', block.button_url, function (v) { block.button_url = v; sync(); }, '/page/'));
    return wrap;
  }

  function renderCalloutFields(block, sync) {
    var wrap = el('div');
    wrap.appendChild(fieldInput('Title', block.title, function (v) { block.title = v; sync(); }));
    wrap.appendChild(fieldTextarea('Body', block.body, function (v) { block.body = v; sync(); }));
    return wrap;
  }

  function renderQuoteFields(block, sync) {
    var wrap = el('div');
    wrap.appendChild(fieldTextarea('Quote', block.quote, function (v) { block.quote = v; sync(); }));
    wrap.appendChild(fieldInput('Author', block.author, function (v) { block.author = v; sync(); }));
    return wrap;
  }

  function renderCodeFields(block, sync) {
    var wrap = el('div');
    wrap.appendChild(fieldTextarea('HTML / Embed Code', block.html, function (v) { block.html = v; sync(); }, '<script>...</script>'));
    var hint = el('p', { textContent: 'Trusted embed. Raw HTML/JS placed directly on the page. Only for trusted admins.', style: 'font-size:0.75rem;color:#adb5bd;margin-top:-0.5rem;' });
    wrap.appendChild(hint);
    return wrap;
  }

  function renderListBlock(block, sync, rerender, config) {
    var wrap = el('div');

    function buildRow(item, index) {
      var row = el('div', { className: 'cms-repeater-row' });
      config.fields.forEach(function (f) {
        var fieldEl = f.multiline
          ? fieldTextarea(f.label, item[f.key], function (v) { item[f.key] = v; sync(); })
          : fieldInput(f.label, item[f.key], function (v) { item[f.key] = v; sync(); });
        row.appendChild(fieldEl);
      });
      var actions = el('div', { className: 'cms-repeater-actions' });
      var removeBtn = el('button', { type: 'button', className: 'cms-btn cms-btn-sm cms-btn-ghost', textContent: 'Remove' });
      removeBtn.addEventListener('click', function () {
        block[config.key].splice(index, 1);
        sync();
        rerender();
      });
      actions.appendChild(removeBtn);
      row.appendChild(actions);
      return row;
    }

    block[config.key].forEach(function (item, i) {
      wrap.appendChild(buildRow(item, i));
    });

    var addBtn = el('button', { type: 'button', className: 'cms-btn cms-btn-sm cms-btn-ghost', textContent: '+ Add Item' });
    addBtn.addEventListener('click', function () {
      var newItem = {};
      config.fields.forEach(function (f) { newItem[f.key] = ''; });
      block[config.key].push(newItem);
      sync();
      rerender();
    });
    wrap.appendChild(addBtn);
    return wrap;
  }

  function renderFeatureGridFields(block, sync, rerender) {
    return renderListBlock(block, sync, rerender, {
      key: 'items',
      fields: [
        { label: 'Title', key: 'title' },
        { label: 'Body', key: 'body', multiline: true },
      ]
    });
  }

  function renderFaqFields(block, sync, rerender) {
    return renderListBlock(block, sync, rerender, {
      key: 'items',
      fields: [
        { label: 'Question', key: 'question' },
        { label: 'Answer', key: 'answer', multiline: true },
      ]
    });
  }

  function renderLogoCloudFields(block, sync, rerender) {
    return renderListBlock(block, sync, rerender, {
      key: 'logos',
      fields: [
        { label: 'Image URL', key: 'src' },
        { label: 'Alt Text', key: 'alt' },
      ]
    });
  }

  function renderImageGalleryFields(block, sync, rerender) {
    var wrap = el('div');
    wrap.appendChild(fieldInput('Gallery Title', block.title, function (v) { block.title = v; sync(); }));

    // Layout select
    var layoutWrap = el('div', { className: 'cms-field' });
    layoutWrap.appendChild(el('label', { textContent: 'Layout' }));
    var sel = el('select', { className: 'cms-input' });
    ['grid', 'masonry', 'carousel'].forEach(function (opt) {
      var o = el('option', { value: opt, textContent: opt });
      if (block.layout === opt) o.selected = true;
      sel.appendChild(o);
    });
    sel.addEventListener('change', function () { block.layout = sel.value; sync(); });
    layoutWrap.appendChild(sel);
    wrap.appendChild(layoutWrap);

    // Images list
    block.images.forEach(function (img, i) {
      var row = el('div', { className: 'cms-repeater-row' });
      row.appendChild(fieldInput('Image URL', img.src, function (v) { img.src = v; sync(); }));
      row.appendChild(fieldInput('Alt Text', img.alt, function (v) { img.alt = v; sync(); }));
      row.appendChild(fieldInput('Caption', img.caption, function (v) { img.caption = v; sync(); }));

      // Upload button
      var uploadLabel = el('label', { className: 'cms-btn cms-btn-sm cms-btn-ghost cms-upload-btn' });
      var fileInput = el('input', { type: 'file', accept: 'image/*', style: 'display:none' });
      uploadLabel.textContent = 'Upload Image';
      uploadLabel.appendChild(fileInput);
      fileInput.addEventListener('change', function () {
        if (!fileInput.files[0]) return;
        uploadLabel.textContent = 'Uploading...';
        window.cmsUploadImage(fileInput.files[0], function (url) {
          img.src = url;
          sync();
          rerender();
        }, function (err) {
          uploadLabel.textContent = 'Upload Image';
          alert('Upload failed: ' + err);
        });
      });

      var actions = el('div', { className: 'cms-repeater-actions' });
      var removeBtn = el('button', { type: 'button', className: 'cms-btn cms-btn-sm cms-btn-ghost', textContent: 'Remove' });
      removeBtn.addEventListener('click', function () {
        block.images.splice(i, 1);
        sync();
        rerender();
      });
      actions.appendChild(uploadLabel);
      actions.appendChild(removeBtn);
      row.appendChild(actions);
      wrap.appendChild(row);
    });

    var addBtn = el('button', { type: 'button', className: 'cms-btn cms-btn-sm cms-btn-ghost', textContent: '+ Add Image' });
    addBtn.addEventListener('click', function () {
      block.images.push({ src: '', alt: '', caption: '' });
      sync();
      rerender();
    });
    wrap.appendChild(addBtn);
    return wrap;
  }

  function renderComparisonTableFields(block, sync, rerender) {
    var wrap = el('div');

    // Headers row
    var headersWrap = el('div', { className: 'cms-field' });
    headersWrap.appendChild(el('label', { textContent: 'Column Headers (comma-separated)' }));
    var headersInput = el('input', { type: 'text', value: block.headers.join(', ') });
    headersInput.addEventListener('change', function () {
      block.headers = headersInput.value.split(',').map(function (s) { return s.trim(); });
      sync();
    });
    headersWrap.appendChild(headersInput);
    wrap.appendChild(headersWrap);

    // Rows
    var rowsLabel = el('p', { textContent: 'Rows:', style: 'font-size:0.8rem;font-weight:600;margin-bottom:0.5rem;' });
    wrap.appendChild(rowsLabel);

    block.rows.forEach(function (row, ri) {
      var rowWrap = el('div', { className: 'cms-repeater-row', style: 'display:flex;gap:0.5rem;align-items:center;' });
      row.forEach(function (cell, ci) {
        var inp = el('input', { type: 'text', value: cell, style: 'flex:1;' });
        inp.placeholder = block.headers[ci] || ('Col ' + (ci + 1));
        inp.addEventListener('input', function () { row[ci] = inp.value; sync(); });
        rowWrap.appendChild(inp);
      });
      var del = el('button', { type: 'button', className: 'cms-btn cms-btn-sm cms-btn-ghost', textContent: '✕' });
      del.addEventListener('click', function () { block.rows.splice(ri, 1); sync(); rerender(); });
      rowWrap.appendChild(del);
      wrap.appendChild(rowWrap);
    });

    var addRow = el('button', { type: 'button', className: 'cms-btn cms-btn-sm cms-btn-ghost', textContent: '+ Add Row' });
    addRow.addEventListener('click', function () {
      block.rows.push(block.headers.map(function () { return ''; }));
      sync();
      rerender();
    });
    wrap.appendChild(addRow);
    return wrap;
  }

  function renderPricingTableFields(block, sync, rerender) {
    var wrap = el('div');

    block.plans.forEach(function (plan, pi) {
      var planWrap = el('div', { className: 'cms-repeater-row' });
      planWrap.appendChild(fieldInput('Plan Name', plan.title, function (v) { plan.title = v; sync(); }));
      planWrap.appendChild(fieldInput('Price', plan.price, function (v) { plan.price = v; sync(); }, '$49/mo'));

      // Features
      var featLabel = el('p', { textContent: 'Features (one per line):', style: 'font-size:0.75rem;font-weight:600;margin:0.5rem 0 0.25rem;' });
      planWrap.appendChild(featLabel);
      var featTa = el('textarea', { placeholder: 'Feature 1\nFeature 2', style: 'width:100%;border:1px solid #dee2e6;border-radius:4px;padding:0.4rem;font-size:0.8rem;min-height:80px;font-family:inherit;' });
      featTa.value = (plan.features || []).join('\n');
      featTa.addEventListener('input', function () {
        plan.features = featTa.value.split('\n').filter(function (l) { return l.trim(); });
        sync();
      });
      planWrap.appendChild(featTa);

      var removeBtn = el('button', { type: 'button', className: 'cms-btn cms-btn-sm cms-btn-ghost', textContent: 'Remove Plan', style: 'margin-top:0.5rem;' });
      removeBtn.addEventListener('click', function () {
        block.plans.splice(pi, 1);
        sync();
        rerender();
      });
      planWrap.appendChild(removeBtn);
      wrap.appendChild(planWrap);
    });

    var addBtn = el('button', { type: 'button', className: 'cms-btn cms-btn-sm cms-btn-ghost', textContent: '+ Add Plan' });
    addBtn.addEventListener('click', function () {
      block.plans.push({ title: '', price: '', features: [''] });
      sync();
      rerender();
    });
    wrap.appendChild(addBtn);
    return wrap;
  }

  // ─── EditorJS Rich Text ──────────────────────────────────────
  var editorInstances = {};

  function renderRichTextFields(block, sync, rerender, blockIndex) {
    var holderId = 'cms-editor-holder-' + blockIndex + '-' + Date.now();
    var holderDiv = el('div', { id: holderId, className: 'cms-editorjs-holder' });

    setTimeout(function () {
      if (typeof EditorJS === 'undefined') {
        holderDiv.innerHTML = '<p style="color:#adb5bd;font-size:0.8rem;">EditorJS not loaded. Add CDN scripts to cms/base.html.</p>';
        return;
      }

      // Destroy existing instance
      if (editorInstances[blockIndex] && editorInstances[blockIndex].destroy) {
        try { editorInstances[blockIndex].destroy(); } catch (e) {}
      }

      var editorData = block.content && block.content.blocks && block.content.blocks.length
        ? block.content
        : { blocks: [] };

      var tools = {};
      if (typeof Header !== 'undefined') tools.header = Header;
      if (typeof List !== 'undefined') tools.list = List;
      if (typeof Quote !== 'undefined') tools.quote = Quote;
      if (typeof Table !== 'undefined') tools.table = Table;
      if (typeof CodeTool !== 'undefined') tools.code = CodeTool;
      if (typeof Delimiter !== 'undefined') tools.delimiter = Delimiter;
      if (typeof Warning !== 'undefined') tools.warning = Warning;

      var editor = new EditorJS({
        holder: holderId,
        data: editorData,
        tools: tools,
        minHeight: 80,
        onChange: function () {
          editor.save().then(function (output) {
            block.content = output;
            sync();
          }).catch(function () {});
        },
      });

      editorInstances[blockIndex] = editor;
    }, 50);

    return holderDiv;
  }

  // ─── Block Field Dispatcher ──────────────────────────────────
  function renderBlockFields(block, sync, rerender, blockIndex) {
    switch (block.type) {
      case 'rich_text':       return renderRichTextFields(block, sync, rerender, blockIndex);
      case 'code':            return renderCodeFields(block, sync);
      case 'cta':             return renderCtaFields(block, sync);
      case 'callout':         return renderCalloutFields(block, sync);
      case 'feature_grid':    return renderFeatureGridFields(block, sync, rerender);
      case 'faq':             return renderFaqFields(block, sync, rerender);
      case 'quote':           return renderQuoteFields(block, sync);
      case 'comparison_table':return renderComparisonTableFields(block, sync, rerender);
      case 'pricing_table':   return renderPricingTableFields(block, sync, rerender);
      case 'logo_cloud':      return renderLogoCloudFields(block, sync, rerender);
      case 'image_gallery':   return renderImageGalleryFields(block, sync, rerender);
      default: return el('p', { textContent: 'Unknown block type: ' + block.type, style: 'color:#adb5bd;' });
    }
  }

  // ─── Add Bar ─────────────────────────────────────────────────
  function createAddBar(insertIndex, state, sync, render) {
    var bar = el('div', { className: 'cms-add-bar' });
    bar.appendChild(el('span', { className: 'cms-add-label', textContent: 'Add:' }));

    BLOCK_TYPES.forEach(function (type) {
      var btn = el('button', { type: 'button', className: 'cms-add-btn', textContent: BLOCK_LABELS[type] });
      btn.addEventListener('click', function () {
        state.blocks.splice(insertIndex, 0, blockDefaults(type));
        sync();
        render();
      });
      bar.appendChild(btn);
    });

    return bar;
  }

  // ─── Main: initBlocksBuilder ─────────────────────────────────
  function initBlocksBuilder() {
    var builderEl = document.querySelector('[data-blocks-builder]');
    var inputEl = document.querySelector('[data-blocks-input]');

    if (!builderEl || !inputEl) return;

    // Parse & normalize state
    var raw = safeJsonParse(inputEl.value);
    var state;
    if (!raw) {
      state = { blocks: [] };
    } else if (Array.isArray(raw)) {
      state = { blocks: raw };
    } else if (raw.blocks && Array.isArray(raw.blocks)) {
      state = raw;
    } else {
      state = { blocks: [] };
    }

    function sync() {
      inputEl.value = JSON.stringify(state);
    }

    var dragSrcIndex = null;

    function render() {
      builderEl.innerHTML = '';

      // Top add bar (inserts at index 0)
      builderEl.appendChild(createAddBar(0, state, sync, render));

      state.blocks.forEach(function (block, index) {
        var item = el('div', { className: 'cms-block-item', draggable: 'true' });

        // Header
        var header = el('div', { className: 'cms-block-header' });

        var dragHandle = el('span', { className: 'cms-block-drag', innerHTML: ICONS.drag });
        dragHandle.title = 'Drag to reorder';
        header.appendChild(dragHandle);

        header.appendChild(el('span', {
          className: 'cms-block-type-badge',
          textContent: BLOCK_LABELS[block.type] || block.type,
        }));

        header.appendChild(el('span', { className: 'cms-block-spacer' }));

        var isCollapsed = false;
        var collapseBtn = el('button', { type: 'button', className: 'cms-block-collapse', innerHTML: ICONS.collapse });
        collapseBtn.title = 'Collapse/expand';
        collapseBtn.addEventListener('click', function () {
          isCollapsed = !isCollapsed;
          body.classList.toggle('collapsed', isCollapsed);
          collapseBtn.innerHTML = isCollapsed ? ICONS.expand : ICONS.collapse;
        });
        header.appendChild(collapseBtn);

        var removeBtn = el('button', { type: 'button', className: 'cms-block-remove', innerHTML: ICONS.remove });
        removeBtn.title = 'Remove block';
        removeBtn.addEventListener('click', function () {
          if (!confirm('Remove this block?')) return;
          if (editorInstances[index] && editorInstances[index].destroy) {
            try { editorInstances[index].destroy(); } catch (e) {}
            delete editorInstances[index];
          }
          state.blocks.splice(index, 1);
          sync();
          render();
        });
        header.appendChild(removeBtn);

        item.appendChild(header);

        // Body
        var body = el('div', { className: 'cms-block-body' });
        body.appendChild(renderBlockFields(block, sync, render, index));
        item.appendChild(body);

        // Drag events
        item.addEventListener('dragstart', function (e) {
          dragSrcIndex = index;
          e.dataTransfer.effectAllowed = 'move';
          setTimeout(function () { item.classList.add('dragging'); }, 0);
        });

        item.addEventListener('dragend', function () {
          item.classList.remove('dragging');
        });

        item.addEventListener('dragover', function (e) {
          e.preventDefault();
          e.dataTransfer.dropEffect = 'move';
          document.querySelectorAll('.cms-block-item').forEach(function (el) {
            el.classList.remove('drag-over');
          });
          item.classList.add('drag-over');
        });

        item.addEventListener('dragleave', function () {
          item.classList.remove('drag-over');
        });

        item.addEventListener('drop', function (e) {
          e.preventDefault();
          item.classList.remove('drag-over');
          if (dragSrcIndex === null || dragSrcIndex === index) return;
          var moved = state.blocks.splice(dragSrcIndex, 1)[0];
          var target = index > dragSrcIndex ? index - 1 : index;
          state.blocks.splice(target, 0, moved);
          dragSrcIndex = null;
          sync();
          render();
        });

        builderEl.appendChild(item);
      });

      // Bottom add bar (appends at end)
      builderEl.appendChild(createAddBar(state.blocks.length, state, sync, render));
    }

    render();

    // ─── Form Submit Hook ────────────────────────────────────
    var form = inputEl.closest('form');
    if (!form) return;

    form.addEventListener('submit', function handleBlocksSubmit(e) {
      e.preventDefault();
      form.removeEventListener('submit', handleBlocksSubmit);

      // Collect all active EditorJS instances
      var saves = Object.keys(editorInstances).map(function (idx) {
        var editor = editorInstances[idx];
        var block = state.blocks[parseInt(idx, 10)];
        if (!editor || !editor.save || !block) return Promise.resolve();
        return editor.save().then(function (output) {
          block.content = output;
        }).catch(function () {});
      });

      Promise.all(saves).then(function () {
        sync();
        form.submit();
      }).catch(function () {
        sync();
        form.submit();
      });
    });
  }

  // ─── Global Upload Helper ────────────────────────────────────
  window.cmsUploadImage = function (file, onSuccess, onError) {
    var csrfMeta = document.querySelector('[name=csrfmiddlewaretoken]');
    var csrf = csrfMeta ? csrfMeta.value : '';
    var fd = new FormData();
    fd.append('file', file);
    fd.append('folder', 'cms/gallery');

    var uploadUrl = document.body.dataset.uploadUrl || '/cms/upload/';

    fetch(uploadUrl, {
      method: 'POST',
      headers: { 'X-CSRFToken': csrf },
      body: fd,
    })
      .then(function (r) { return r.json(); })
      .then(function (data) {
        if (data.url) onSuccess(data.url);
        else onError(data.error || 'Unknown error');
      })
      .catch(function (err) { onError(err.message); });
  };

  // ─── Cloudinary Upload Widgets ───────────────────────────────
  function initUploadWidgets() {
    var widgets = document.querySelectorAll('.cms-cloudinary-upload');
    widgets.forEach(function (widget) {
      var targetId = widget.dataset.target;
      var hiddenInput = document.getElementById(targetId);
      var preview = widget.querySelector('.cms-upload-preview');
      var statusEl = widget.querySelector('.cms-upload-status');
      var fileInput = widget.querySelector('[data-upload-trigger]');

      if (!fileInput || !hiddenInput) return;

      fileInput.addEventListener('change', function () {
        if (!fileInput.files[0]) return;
        if (statusEl) statusEl.textContent = 'Uploading…';

        window.cmsUploadImage(fileInput.files[0], function (url) {
          hiddenInput.value = url;
          if (preview) {
            preview.innerHTML = '<img src="' + url + '" style="max-height:120px;border-radius:6px;">';
          }
          if (statusEl) statusEl.textContent = 'Uploaded ✓';
        }, function (err) {
          if (statusEl) statusEl.textContent = 'Error: ' + err;
        });
      });
    });
  }

  // ─── SEO Toggle ──────────────────────────────────────────────
  function initSeoToggle() {
    var btn = document.querySelector('.cms-seo-toggle');
    var body = document.querySelector('.cms-seo-body');
    if (!btn || !body) return;
    btn.addEventListener('click', function () {
      body.classList.toggle('open');
      btn.querySelector('.cms-seo-toggle-icon').textContent = body.classList.contains('open') ? '▲' : '▼';
    });
  }

  // ─── Delete Confirm ──────────────────────────────────────────
  function initDeleteConfirm() {
    var showBtn = document.querySelector('[data-show-delete-confirm]');
    var banner = document.querySelector('.cms-confirm-delete');
    var cancelBtn = document.querySelector('[data-cancel-delete]');

    if (!showBtn || !banner) return;

    showBtn.addEventListener('click', function () {
      banner.classList.add('visible');
      banner.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });

    if (cancelBtn) {
      cancelBtn.addEventListener('click', function () {
        banner.classList.remove('visible');
      });
    }
  }

  // ─── Init ────────────────────────────────────────────────────
  document.addEventListener('DOMContentLoaded', function () {
    initBlocksBuilder();
    initUploadWidgets();
    initSeoToggle();
    initDeleteConfirm();
  });

})();
