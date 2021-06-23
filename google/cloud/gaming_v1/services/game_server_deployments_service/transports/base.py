# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
import packaging.version
import pkg_resources

import google.auth  # type: ignore
import google.api_core  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.gaming_v1.types import game_server_deployments
from google.longrunning import operations_pb2  # type: ignore

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-game-servers",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()

try:
    # google.auth.__version__ was added in 1.26.0
    _GOOGLE_AUTH_VERSION = google.auth.__version__
except AttributeError:
    try:  # try pkg_resources if it is available
        _GOOGLE_AUTH_VERSION = pkg_resources.get_distribution("google-auth").version
    except pkg_resources.DistributionNotFound:  # pragma: NO COVER
        _GOOGLE_AUTH_VERSION = None


class GameServerDeploymentsServiceTransport(abc.ABC):
    """Abstract transport class for GameServerDeploymentsService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "gameservices.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        scopes_kwargs = self._get_scopes_kwargs(self._host, scopes)

        # Save the scopes.
        self._scopes = scopes or self.AUTH_SCOPES

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file, **scopes_kwargs, quota_project_id=quota_project_id
            )

        elif credentials is None:
            credentials, _ = google.auth.default(
                **scopes_kwargs, quota_project_id=quota_project_id
            )

        # If the credentials is service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

    # TODO(busunkim): This method is in the base transport
    # to avoid duplicating code across the transport classes. These functions
    # should be deleted once the minimum required versions of google-auth is increased.

    # TODO: Remove this function once google-auth >= 1.25.0 is required
    @classmethod
    def _get_scopes_kwargs(
        cls, host: str, scopes: Optional[Sequence[str]]
    ) -> Dict[str, Optional[Sequence[str]]]:
        """Returns scopes kwargs to pass to google-auth methods depending on the google-auth version"""

        scopes_kwargs = {}

        if _GOOGLE_AUTH_VERSION and (
            packaging.version.parse(_GOOGLE_AUTH_VERSION)
            >= packaging.version.parse("1.25.0")
        ):
            scopes_kwargs = {"scopes": scopes, "default_scopes": cls.AUTH_SCOPES}
        else:
            scopes_kwargs = {"scopes": scopes or cls.AUTH_SCOPES}

        return scopes_kwargs

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.list_game_server_deployments: gapic_v1.method.wrap_method(
                self.list_game_server_deployments,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_game_server_deployment: gapic_v1.method.wrap_method(
                self.get_game_server_deployment,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_game_server_deployment: gapic_v1.method.wrap_method(
                self.create_game_server_deployment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_game_server_deployment: gapic_v1.method.wrap_method(
                self.delete_game_server_deployment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_game_server_deployment: gapic_v1.method.wrap_method(
                self.update_game_server_deployment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_game_server_deployment_rollout: gapic_v1.method.wrap_method(
                self.get_game_server_deployment_rollout,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_game_server_deployment_rollout: gapic_v1.method.wrap_method(
                self.update_game_server_deployment_rollout,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.preview_game_server_deployment_rollout: gapic_v1.method.wrap_method(
                self.preview_game_server_deployment_rollout,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.fetch_deployment_state: gapic_v1.method.wrap_method(
                self.fetch_deployment_state,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
        }

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def list_game_server_deployments(
        self,
    ) -> Callable[
        [game_server_deployments.ListGameServerDeploymentsRequest],
        Union[
            game_server_deployments.ListGameServerDeploymentsResponse,
            Awaitable[game_server_deployments.ListGameServerDeploymentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_game_server_deployment(
        self,
    ) -> Callable[
        [game_server_deployments.GetGameServerDeploymentRequest],
        Union[
            game_server_deployments.GameServerDeployment,
            Awaitable[game_server_deployments.GameServerDeployment],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_game_server_deployment(
        self,
    ) -> Callable[
        [game_server_deployments.CreateGameServerDeploymentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_game_server_deployment(
        self,
    ) -> Callable[
        [game_server_deployments.DeleteGameServerDeploymentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_game_server_deployment(
        self,
    ) -> Callable[
        [game_server_deployments.UpdateGameServerDeploymentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_game_server_deployment_rollout(
        self,
    ) -> Callable[
        [game_server_deployments.GetGameServerDeploymentRolloutRequest],
        Union[
            game_server_deployments.GameServerDeploymentRollout,
            Awaitable[game_server_deployments.GameServerDeploymentRollout],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_game_server_deployment_rollout(
        self,
    ) -> Callable[
        [game_server_deployments.UpdateGameServerDeploymentRolloutRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def preview_game_server_deployment_rollout(
        self,
    ) -> Callable[
        [game_server_deployments.PreviewGameServerDeploymentRolloutRequest],
        Union[
            game_server_deployments.PreviewGameServerDeploymentRolloutResponse,
            Awaitable[
                game_server_deployments.PreviewGameServerDeploymentRolloutResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_deployment_state(
        self,
    ) -> Callable[
        [game_server_deployments.FetchDeploymentStateRequest],
        Union[
            game_server_deployments.FetchDeploymentStateResponse,
            Awaitable[game_server_deployments.FetchDeploymentStateResponse],
        ],
    ]:
        raise NotImplementedError()


__all__ = ("GameServerDeploymentsServiceTransport",)
