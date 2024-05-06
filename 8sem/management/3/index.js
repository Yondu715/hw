const LS_DATA = 'data';
const lastnameRegex = '[А-ЯЁ][а-яё]+';
const initialsRegex = '[А-ЯЁ]\\.\\s[А-ЯЁ]\\.';
const addressRegex = '[А-Яа-я0-9,\\-.\\s]+';

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
    const deliveryType = form.querySelector("input[name='delivery_type']:checked").value;
    const needInvoice = form.querySelector("input[name='invoice']").checked;
    const adding = form.querySelector("textarea[name='adding']").value;
    console.log(lastname);
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

const checkLastName = () => {
    const lastname = form.querySelector("input[name='lastname']").value;
    if (!lastname.match(lastnameRegex)) {
        alert("Неправильно введена фамилия");
        return false;
    }
    return true;
}

const checkInitials = () => {
    const initials = form.querySelector("input[name='initials']").value;
    if (!initials.match(initialsRegex)) {
        alert("Неправильно введены инициалы. Необходим ввод типа: И. И.");
        return false;
    }
    return true;
}

const checkAddress = () => {
    const address = form.querySelector("input[name='address']").value;
    if (!address.match(addressRegex)) {
        alert("Неправильно введен адрес");
        return false;
    }
    return true;
}

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
    if (!checkLastName() || !checkInitials() || !checkAddress()) return;
    const accepted = confirm('Подтвердите отправку формы');
    accepted && submitForm(e.currentTarget);
})