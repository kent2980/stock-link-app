<<<<<<< HEAD:frontend/src/client/schemas.ts
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
	type: 'MetricItems',
	isRequired: true,
},
		upperMetrics: {
	type: 'MetricItems',
	isRequired: true,
},
		lowerMetrics: {
	type: 'MetricItems',
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

export const $MetricItems = {
	properties: {
		is_active: {
	type: 'boolean',
	default: false,
},
		data: {
	type: 'any-of',
	contains: [{
	type: 'array',
	contains: {
		type: 'MetricParentSchema',
	},
}, {
	type: 'null',
}],
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
=======
// This file is auto-generated by @hey-api/openapi-ts

export const Body_login_login_access_tokenSchema = {
  properties: {
    grant_type: {
      anyOf: [
        {
          type: "string",
          pattern: "password",
        },
        {
          type: "null",
        },
      ],
      title: "Grant Type",
    },
    username: {
      type: "string",
      title: "Username",
    },
    password: {
      type: "string",
      title: "Password",
    },
    scope: {
      type: "string",
      title: "Scope",
      default: "",
    },
    client_id: {
      anyOf: [
        {
          type: "string",
        },
        {
          type: "null",
        },
      ],
      title: "Client Id",
    },
    client_secret: {
      anyOf: [
        {
          type: "string",
        },
        {
          type: "null",
        },
      ],
      title: "Client Secret",
    },
  },
  type: "object",
  required: ["username", "password"],
  title: "Body_login-login_access_token",
} as const

export const HTTPValidationErrorSchema = {
  properties: {
    detail: {
      items: {
        $ref: "#/components/schemas/ValidationError",
      },
      type: "array",
      title: "Detail",
    },
  },
  type: "object",
  title: "HTTPValidationError",
} as const

export const ItemCreateSchema = {
  properties: {
    title: {
      type: "string",
      maxLength: 255,
      minLength: 1,
      title: "Title",
    },
    description: {
      anyOf: [
        {
          type: "string",
          maxLength: 255,
        },
        {
          type: "null",
        },
      ],
      title: "Description",
    },
  },
  type: "object",
  required: ["title"],
  title: "ItemCreate",
} as const

export const ItemPublicSchema = {
  properties: {
    title: {
      type: "string",
      maxLength: 255,
      minLength: 1,
      title: "Title",
    },
    description: {
      anyOf: [
        {
          type: "string",
          maxLength: 255,
        },
        {
          type: "null",
        },
      ],
      title: "Description",
    },
    id: {
      type: "string",
      format: "uuid",
      title: "Id",
    },
    owner_id: {
      type: "string",
      format: "uuid",
      title: "Owner Id",
    },
  },
  type: "object",
  required: ["title", "id", "owner_id"],
  title: "ItemPublic",
} as const

export const ItemUpdateSchema = {
  properties: {
    title: {
      anyOf: [
        {
          type: "string",
          maxLength: 255,
          minLength: 1,
        },
        {
          type: "null",
        },
      ],
      title: "Title",
    },
    description: {
      anyOf: [
        {
          type: "string",
          maxLength: 255,
        },
        {
          type: "null",
        },
      ],
      title: "Description",
    },
  },
  type: "object",
  title: "ItemUpdate",
} as const

export const ItemsPublicSchema = {
  properties: {
    data: {
      items: {
        $ref: "#/components/schemas/ItemPublic",
      },
      type: "array",
      title: "Data",
    },
    count: {
      type: "integer",
      title: "Count",
    },
  },
  type: "object",
  required: ["data", "count"],
  title: "ItemsPublic",
} as const

export const MessageSchema = {
  properties: {
    message: {
      type: "string",
      title: "Message",
    },
  },
  type: "object",
  required: ["message"],
  title: "Message",
} as const

export const NewPasswordSchema = {
  properties: {
    token: {
      type: "string",
      title: "Token",
    },
    new_password: {
      type: "string",
      maxLength: 40,
      minLength: 8,
      title: "New Password",
    },
  },
  type: "object",
  required: ["token", "new_password"],
  title: "NewPassword",
} as const

export const TokenSchema = {
  properties: {
    access_token: {
      type: "string",
      title: "Access Token",
    },
    token_type: {
      type: "string",
      title: "Token Type",
      default: "bearer",
    },
  },
  type: "object",
  required: ["access_token"],
  title: "Token",
} as const

export const UpdatePasswordSchema = {
  properties: {
    current_password: {
      type: "string",
      maxLength: 40,
      minLength: 8,
      title: "Current Password",
    },
    new_password: {
      type: "string",
      maxLength: 40,
      minLength: 8,
      title: "New Password",
    },
  },
  type: "object",
  required: ["current_password", "new_password"],
  title: "UpdatePassword",
} as const

export const UserCreateSchema = {
  properties: {
    email: {
      type: "string",
      maxLength: 255,
      format: "email",
      title: "Email",
    },
    is_active: {
      type: "boolean",
      title: "Is Active",
      default: true,
    },
    is_superuser: {
      type: "boolean",
      title: "Is Superuser",
      default: false,
    },
    full_name: {
      anyOf: [
        {
          type: "string",
          maxLength: 255,
        },
        {
          type: "null",
        },
      ],
      title: "Full Name",
    },
    password: {
      type: "string",
      maxLength: 40,
      minLength: 8,
      title: "Password",
    },
  },
  type: "object",
  required: ["email", "password"],
  title: "UserCreate",
} as const

export const UserPublicSchema = {
  properties: {
    email: {
      type: "string",
      maxLength: 255,
      format: "email",
      title: "Email",
    },
    is_active: {
      type: "boolean",
      title: "Is Active",
      default: true,
    },
    is_superuser: {
      type: "boolean",
      title: "Is Superuser",
      default: false,
    },
    full_name: {
      anyOf: [
        {
          type: "string",
          maxLength: 255,
        },
        {
          type: "null",
        },
      ],
      title: "Full Name",
    },
    id: {
      type: "string",
      format: "uuid",
      title: "Id",
    },
  },
  type: "object",
  required: ["email", "id"],
  title: "UserPublic",
} as const

export const UserRegisterSchema = {
  properties: {
    email: {
      type: "string",
      maxLength: 255,
      format: "email",
      title: "Email",
    },
    password: {
      type: "string",
      maxLength: 40,
      minLength: 8,
      title: "Password",
    },
    full_name: {
      anyOf: [
        {
          type: "string",
          maxLength: 255,
        },
        {
          type: "null",
        },
      ],
      title: "Full Name",
    },
  },
  type: "object",
  required: ["email", "password"],
  title: "UserRegister",
} as const

export const UserUpdateSchema = {
  properties: {
    email: {
      anyOf: [
        {
          type: "string",
          maxLength: 255,
          format: "email",
        },
        {
          type: "null",
        },
      ],
      title: "Email",
    },
    is_active: {
      type: "boolean",
      title: "Is Active",
      default: true,
    },
    is_superuser: {
      type: "boolean",
      title: "Is Superuser",
      default: false,
    },
    full_name: {
      anyOf: [
        {
          type: "string",
          maxLength: 255,
        },
        {
          type: "null",
        },
      ],
      title: "Full Name",
    },
    password: {
      anyOf: [
        {
          type: "string",
          maxLength: 40,
          minLength: 8,
        },
        {
          type: "null",
        },
      ],
      title: "Password",
    },
  },
  type: "object",
  title: "UserUpdate",
} as const

export const UserUpdateMeSchema = {
  properties: {
    full_name: {
      anyOf: [
        {
          type: "string",
          maxLength: 255,
        },
        {
          type: "null",
        },
      ],
      title: "Full Name",
    },
    email: {
      anyOf: [
        {
          type: "string",
          maxLength: 255,
          format: "email",
        },
        {
          type: "null",
        },
      ],
      title: "Email",
    },
  },
  type: "object",
  title: "UserUpdateMe",
} as const

export const UsersPublicSchema = {
  properties: {
    data: {
      items: {
        $ref: "#/components/schemas/UserPublic",
      },
      type: "array",
      title: "Data",
    },
    count: {
      type: "integer",
      title: "Count",
    },
  },
  type: "object",
  required: ["data", "count"],
  title: "UsersPublic",
} as const

export const ValidationErrorSchema = {
  properties: {
    loc: {
      items: {
        anyOf: [
          {
            type: "string",
          },
          {
            type: "integer",
          },
        ],
      },
      type: "array",
      title: "Location",
    },
    msg: {
      type: "string",
      title: "Message",
    },
    type: {
      type: "string",
      title: "Error Type",
    },
  },
  type: "object",
  required: ["loc", "msg", "type"],
  title: "ValidationError",
} as const
>>>>>>> 6efd3ba9a0c4cc7e6beb8af416a58e7a31a13ef2:frontend/src/client/schemas.gen.ts
