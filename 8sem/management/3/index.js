const LS_DATA = 'data';

const clearForm = () => {
    document.getElementById('form').reset();
}

const getDataFromForm = (form) => {
    const lastname = form.querySelector("input[name='lastname']").value;
    const initials = form.querySelector("input[name='initials']").value;
    const password = form.querySelector("input[name='password']").value;
    const address = form.querySelector("input[name='address']").value;
    const count = form.querySelector("input[name='count']").value;
    const typeFirst = form.querySelector("select[name='type_first']").value;
    const typeSecond = form.querySelector("select[name='type_second']").value;
    const deliveryType = form.querySelector("input[name='delivery_type']").value;
    const needInvoice = form.querySelector("input[name='invoice']").checked;
    const adding = form.querySelector("textarea[name='adding']").value;

    return {
        lastname,
        initials,
        password,
        address,
        count,
        typeFirst,
        typeSecond,
        deliveryType,
        needInvoice,
        adding
    };
}

const getExcelHeader = () => {
    return [
        'Фамилия',
        'Инициалы',
        'Пароль',
        'Адрес получателя',
        'Количество',
        'Тип_1',
        'Тип_2',
        'Доставка',
        'Требуется накладная',
        'Дополнительная информация',
    ];
}

const exportToExcel = (data) => {
    let array = data;
    if (!Array.isArray(array)) {
        array = [data];
    }
    const worksheet = XLSX.utils.json_to_sheet(data);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.sheet_add_aoa(worksheet, [getExcelHeader()], { origin: "A1" });
    XLSX.utils.book_append_sheet(workbook, worksheet, "Orders");
    XLSX.writeFile(workbook, "orders.xlsx", { compression: true });
};

const submitForm = (form) => {
    const data = getDataFromForm(form);
    const storageData = localStorage.getItem(LS_DATA) ? JSON.parse(localStorage.getItem(LS_DATA)) : [];
    const assignedData = [data, ...storageData];
    localStorage.setItem(LS_DATA, JSON.stringify(assignedData));
};

const downloadReport = () => {
    const storageData = localStorage.getItem(LS_DATA) ? JSON.parse(localStorage.getItem(LS_DATA)) : [];
    exportToExcel(storageData);
};

document.getElementById('form').addEventListener('submit', (e) => {
    e.preventDefault();
    const accepted = confirm('Подтвердите отправку формы');
    accepted && submitForm(e.currentTarget);
})