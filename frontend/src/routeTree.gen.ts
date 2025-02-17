/* prettier-ignore-start */

/* eslint-disable */

// @ts-nocheck

// noinspection JSUnusedGlobalSymbols

// This file is auto-generated by TanStack Router

// Import Routes

import { Route as rootRoute } from './routes/__root'
import { Route as SignupImport } from './routes/signup'
import { Route as ResetPasswordImport } from './routes/reset-password'
import { Route as RecoverPasswordImport } from './routes/recover-password'
import { Route as LoginImport } from './routes/login'
import { Route as LayoutImport } from './routes/_layout'
import { Route as LayoutIndexImport } from './routes/_layout/index'
import { Route as LayoutSettingsImport } from './routes/_layout/settings'
import { Route as LayoutItemsImport } from './routes/_layout/items'
import { Route as LayoutIndustriesImport } from './routes/_layout/industries'
import { Route as LayoutAdminImport } from './routes/_layout/admin'
import { Route as LayoutSummaryIndexImport } from './routes/_layout/summary/index'
import { Route as LayoutSummaryCodeLayoutImport } from './routes/_layout/summary/$code/_layout'
import { Route as LayoutSummaryCodeLayoutStockInfoImport } from './routes/_layout/summary/$code/_layout/stockInfo'
import { Route as LayoutSummaryCodeLayoutHeadKeySummaryImport } from './routes/_layout/summary/$code/_layout/$headKey/summary'

// Create/Update Routes

const SignupRoute = SignupImport.update({
  path: '/signup',
  getParentRoute: () => rootRoute,
} as any)

const ResetPasswordRoute = ResetPasswordImport.update({
  path: '/reset-password',
  getParentRoute: () => rootRoute,
} as any)

const RecoverPasswordRoute = RecoverPasswordImport.update({
  path: '/recover-password',
  getParentRoute: () => rootRoute,
} as any)

const LoginRoute = LoginImport.update({
  path: '/login',
  getParentRoute: () => rootRoute,
} as any)

const LayoutRoute = LayoutImport.update({
  id: '/_layout',
  getParentRoute: () => rootRoute,
} as any)

const LayoutIndexRoute = LayoutIndexImport.update({
  path: '/',
  getParentRoute: () => LayoutRoute,
} as any)

const LayoutSettingsRoute = LayoutSettingsImport.update({
  path: '/settings',
  getParentRoute: () => LayoutRoute,
} as any)

const LayoutItemsRoute = LayoutItemsImport.update({
  path: '/items',
  getParentRoute: () => LayoutRoute,
} as any)

const LayoutIndustriesRoute = LayoutIndustriesImport.update({
  path: '/industries',
  getParentRoute: () => LayoutRoute,
} as any)

const LayoutAdminRoute = LayoutAdminImport.update({
  path: '/admin',
  getParentRoute: () => LayoutRoute,
} as any)

const LayoutSummaryIndexRoute = LayoutSummaryIndexImport.update({
  path: '/summary/',
  getParentRoute: () => LayoutRoute,
} as any)

const LayoutSummaryCodeLayoutRoute = LayoutSummaryCodeLayoutImport.update({
  path: '/summary/$code/layout',
  getParentRoute: () => LayoutRoute,
} as any)

const LayoutSummaryCodeLayoutStockInfoRoute =
  LayoutSummaryCodeLayoutStockInfoImport.update({
    path: '/stockInfo',
    getParentRoute: () => LayoutSummaryCodeLayoutRoute,
  } as any)

const LayoutSummaryCodeLayoutHeadKeySummaryRoute =
  LayoutSummaryCodeLayoutHeadKeySummaryImport.update({
    path: '/$headKey/summary',
    getParentRoute: () => LayoutSummaryCodeLayoutRoute,
  } as any)

// Populate the FileRoutesByPath interface

declare module '@tanstack/react-router' {
  interface FileRoutesByPath {
    '/_layout': {
      preLoaderRoute: typeof LayoutImport
      parentRoute: typeof rootRoute
    }
    '/login': {
      preLoaderRoute: typeof LoginImport
      parentRoute: typeof rootRoute
    }
    '/recover-password': {
      preLoaderRoute: typeof RecoverPasswordImport
      parentRoute: typeof rootRoute
    }
    '/reset-password': {
      preLoaderRoute: typeof ResetPasswordImport
      parentRoute: typeof rootRoute
    }
    '/signup': {
      preLoaderRoute: typeof SignupImport
      parentRoute: typeof rootRoute
    }
    '/_layout/admin': {
      preLoaderRoute: typeof LayoutAdminImport
      parentRoute: typeof LayoutImport
    }
    '/_layout/industries': {
      preLoaderRoute: typeof LayoutIndustriesImport
      parentRoute: typeof LayoutImport
    }
    '/_layout/items': {
      preLoaderRoute: typeof LayoutItemsImport
      parentRoute: typeof LayoutImport
    }
    '/_layout/settings': {
      preLoaderRoute: typeof LayoutSettingsImport
      parentRoute: typeof LayoutImport
    }
    '/_layout/': {
      preLoaderRoute: typeof LayoutIndexImport
      parentRoute: typeof LayoutImport
    }
    '/_layout/summary/': {
      preLoaderRoute: typeof LayoutSummaryIndexImport
      parentRoute: typeof LayoutImport
    }
    '/_layout/summary/$code/_layout': {
      preLoaderRoute: typeof LayoutSummaryCodeLayoutImport
      parentRoute: typeof LayoutImport
    }
    '/_layout/summary/$code/_layout/stockInfo': {
      preLoaderRoute: typeof LayoutSummaryCodeLayoutStockInfoImport
      parentRoute: typeof LayoutSummaryCodeLayoutImport
    }
    '/_layout/summary/$code/_layout/$headKey/summary': {
      preLoaderRoute: typeof LayoutSummaryCodeLayoutHeadKeySummaryImport
      parentRoute: typeof LayoutSummaryCodeLayoutImport
    }
  }
}

// Create and export the route tree

export const routeTree = rootRoute.addChildren([
  LayoutRoute.addChildren([
    LayoutAdminRoute,
    LayoutIndustriesRoute,
    LayoutItemsRoute,
    LayoutSettingsRoute,
    LayoutIndexRoute,
    LayoutSummaryIndexRoute,
    LayoutSummaryCodeLayoutRoute.addChildren([
      LayoutSummaryCodeLayoutStockInfoRoute,
      LayoutSummaryCodeLayoutHeadKeySummaryRoute,
    ]),
  ]),
  LoginRoute,
  RecoverPasswordRoute,
  ResetPasswordRoute,
  SignupRoute,
])

/* prettier-ignore-end */
