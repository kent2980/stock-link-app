export const $Body_login_login_access_token = {
	properties: {
		grant_type: {
	type: 'any-of',
	contains: [{
	type: 'string',
	pattern: 'password',
}, {
	type: 'null',
}],
},
		username: {
	type: 'string',
	isRequired: true,
},
		password: {
	type: 'string',
	isRequired: true,
},
		scope: {
	type: 'string',
	default: '',
},
		client_id: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
		client_secret: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $FinancialResponseListSchema = {
	properties: {
		count: {
	type: 'number',
	isRequired: true,
},
		labels: {
	type: 'array',
	contains: {
		type: 'LabelItemSchema',
	},
	isRequired: true,
},
		data: {
	type: 'array',
	contains: {
		type: 'FinancialResponseSchema',
	},
	isRequired: true,
},
	},
} as const;

export const $FinancialResponseSchema = {
	properties: {
		period: {
	type: 'PeriodSchema',
	isRequired: true,
},
		metrics: {
	type: 'array',
	contains: {
		type: 'MetricParentSchema',
	},
	isRequired: true,
},
	},
} as const;

export const $HTTPValidationError = {
	properties: {
		detail: {
	type: 'array',
	contains: {
		type: 'ValidationError',
	},
},
	},
} as const;

export const $IndustriesList = {
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'Industry',
	},
	isRequired: true,
},
	},
} as const;

export const $Industry = {
	properties: {
		code: {
	type: 'number',
	isRequired: true,
},
		name: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $ItemPublic = {
	properties: {
		title: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
	minLength: 1,
},
		description: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
		id: {
	type: 'string',
	isRequired: true,
	format: 'uuid',
},
		owner_id: {
	type: 'string',
	isRequired: true,
	format: 'uuid',
},
	},
} as const;

export const $ItemUpdate = {
	properties: {
		title: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
	minLength: 1,
}, {
	type: 'null',
}],
},
		description: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
	},
} as const;

export const $JpxStockInfoPublic = {
	properties: {
		input_date: {
	type: 'string',
	isRequired: true,
},
		code: {
	type: 'string',
	isRequired: true,
},
		name: {
	type: 'string',
	isRequired: true,
},
		market_or_type: {
	type: 'string',
	isRequired: true,
},
		industry_33_code: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
	isRequired: true,
},
		industry_33_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		industry_17_code: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
	isRequired: true,
},
		industry_17_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		scale_code: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
	isRequired: true,
},
		scale_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $JpxStockInfosPublicList = {
	properties: {
		count: {
	type: 'number',
	isRequired: true,
},
		data: {
	type: 'array',
	contains: {
		type: 'JpxStockInfoPublic',
	},
	isRequired: true,
},
	},
} as const;

export const $LabelItemSchema = {
	properties: {
		label: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $Message = {
	properties: {
		message: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $MetricParentSchema = {
	properties: {
		name: {
	type: 'string',
	isRequired: true,
},
		order: {
	type: 'number',
	isRequired: true,
},
		label: {
	type: 'string',
	isRequired: true,
},
		value: {
	type: 'any-of',
	contains: [{
	type: 'MetricSchema',
}, {
	type: 'null',
}],
},
		change: {
	type: 'any-of',
	contains: [{
	type: 'MetricSchema',
}, {
	type: 'null',
}],
},
	},
} as const;

export const $MetricSchema = {
	properties: {
		key: {
	type: 'string',
	isRequired: true,
},
		name: {
	type: 'string',
	isRequired: true,
},
		value: {
	type: 'any-of',
	contains: [{
	type: 'number',
}, {
	type: 'null',
}],
	isRequired: true,
},
		unit: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $NewPassword = {
	properties: {
		token: {
	type: 'string',
	isRequired: true,
},
		new_password: {
	type: 'string',
	isRequired: true,
	maxLength: 40,
	minLength: 8,
},
	},
} as const;

export const $PeriodSchema = {
	properties: {
		accountingStandard: {
	type: 'string',
	isRequired: true,
},
		fiscalYear: {
	type: 'string',
	isRequired: true,
},
		period: {
	type: 'string',
	isRequired: true,
},
	},
} as const;

export const $StockWikiCreate = {
	description: `StockWikiCreate`,
	properties: {
		code: {
	type: 'string',
	isRequired: true,
	maxLength: 5,
},
		name: {
	type: 'string',
	isRequired: true,
	maxLength: 255,
},
		description: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		url: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $StockWikiPublic = {
	description: `StockWikiPublic`,
	properties: {
		code: {
	type: 'string',
	isRequired: true,
},
		name: {
	type: 'string',
	isRequired: true,
},
		description: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
		url: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'null',
}],
	isRequired: true,
},
	},
} as const;

export const $StockWikisPublicList = {
	description: `StockWikisPublicList`,
	properties: {
		count: {
	type: 'number',
	isRequired: true,
},
		data: {
	type: 'array',
	contains: {
		type: 'StockWikiPublic',
	},
	isRequired: true,
},
	},
} as const;

export const $Token = {
	properties: {
		access_token: {
	type: 'string',
	isRequired: true,
},
		token_type: {
	type: 'string',
	default: 'bearer',
},
	},
} as const;

export const $UpdatePassword = {
	properties: {
		current_password: {
	type: 'string',
	isRequired: true,
	maxLength: 40,
	minLength: 8,
},
		new_password: {
	type: 'string',
	isRequired: true,
	maxLength: 40,
	minLength: 8,
},
	},
} as const;

export const $UserCreate = {
	properties: {
		email: {
	type: 'string',
	isRequired: true,
	format: 'email',
	maxLength: 255,
},
		is_active: {
	type: 'boolean',
	default: true,
},
		is_superuser: {
	type: 'boolean',
	default: false,
},
		full_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
		password: {
	type: 'string',
	isRequired: true,
	maxLength: 40,
	minLength: 8,
},
	},
} as const;

export const $UserPublic = {
	properties: {
		email: {
	type: 'string',
	isRequired: true,
	format: 'email',
	maxLength: 255,
},
		is_active: {
	type: 'boolean',
	default: true,
},
		is_superuser: {
	type: 'boolean',
	default: false,
},
		full_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
		id: {
	type: 'string',
	isRequired: true,
	format: 'uuid',
},
	},
} as const;

export const $UserRegister = {
	properties: {
		email: {
	type: 'string',
	isRequired: true,
	format: 'email',
	maxLength: 255,
},
		password: {
	type: 'string',
	isRequired: true,
	maxLength: 40,
	minLength: 8,
},
		full_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
	},
} as const;

export const $UserUpdate = {
	properties: {
		email: {
	type: 'any-of',
	contains: [{
	type: 'string',
	format: 'email',
	maxLength: 255,
}, {
	type: 'null',
}],
},
		is_active: {
	type: 'boolean',
	default: true,
},
		is_superuser: {
	type: 'boolean',
	default: false,
},
		full_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
		password: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 40,
	minLength: 8,
}, {
	type: 'null',
}],
},
	},
} as const;

export const $UserUpdateMe = {
	properties: {
		full_name: {
	type: 'any-of',
	contains: [{
	type: 'string',
	maxLength: 255,
}, {
	type: 'null',
}],
},
		email: {
	type: 'any-of',
	contains: [{
	type: 'string',
	format: 'email',
	maxLength: 255,
}, {
	type: 'null',
}],
},
	},
} as const;

export const $UsersPublic = {
	properties: {
		data: {
	type: 'array',
	contains: {
		type: 'UserPublic',
	},
	isRequired: true,
},
		count: {
	type: 'number',
	isRequired: true,
},
	},
} as const;

export const $ValidationError = {
	properties: {
		loc: {
	type: 'array',
	contains: {
	type: 'any-of',
	contains: [{
	type: 'string',
}, {
	type: 'number',
}],
},
	isRequired: true,
},
		msg: {
	type: 'string',
	isRequired: true,
},
		type: {
	type: 'string',
	isRequired: true,
},
	},
} as const;